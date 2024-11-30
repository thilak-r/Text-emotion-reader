from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

app = Flask(__name__)

# Load the trained model
model = load_model('emotion_model_1.h5')
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
# Load the tokenizer and label encoder
with open('tokenizer.pkl', 'rb') as file:
    tokenizer = pickle.load(file)

with open('label_encoder.pkl', 'rb') as file:
    label_en = pickle.load(file)

# Set the max_len to 66 as expected by the model
max_len = 66

emotion_labels = {
    0: "anger",
    1: "fear",
    2: "love",
    3: "joy",
    4: "sadness",
    5: "surprise"
}

@app.route('/')
def home():
    return render_template('index.html')  # Ensure you have an index.html file

@app.route('/predict', methods=['POST'])
def predict_emotion():
    if request.is_json:
        # If the request is JSON, get the input_text from JSON data
        data = request.get_json()
        input_text = data.get('text')
    else:
        # If the request is from a form submission, get the input_text from form data
        input_text = request.form.get('text')

    if input_text:
        # Convert the input text into a sequence of integers using the tokenizer
        input_seq = tokenizer.texts_to_sequences([input_text])

        # Pad the input sequence to the max_len (66)
        padded_input_sequence = pad_sequences(input_seq, maxlen=max_len, padding='post')

        # Use the trained model to predict the emotion
        prediction = model.predict(padded_input_sequence)

        # Get index of the class with the highest predicted probability
        predicted_label = np.argmax(prediction)


        predicted_emotion = str(emotion_labels[predicted_label])
        
        if request.is_json:
            return jsonify({'emotion': predicted_emotion})
        else:
            return render_template('result.html', prediction=predicted_emotion)
    else:
        return 'No input text provided', 400

if __name__ == '__main__':
    app.run(debug=True)
