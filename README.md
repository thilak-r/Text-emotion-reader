# Text Emotion Reader 📖💬

**Text Emotion Reader** is a machine learning-powered application designed to analyze the emotional tone of text inputs. Simply provide a text input, and the system will predict the associated emotion, such as *happy*, *sad*, *angry*, and more.

## ✨ Features

- **Emotion Classification**: Classifies text into predefined emotional categories.
- **Pre-trained Models**: Leverages a trained machine learning model for predictions.
- **Real-time Detection**: Provides instant emotion analysis results via a user-friendly interface.

---

## 📂 Project Structure

The repository is organized as follows:

├───static <br>
│   └───css<br>
└───templates<br>
- `static/css/` - CSS files for styling the web interface.
- `templates/` - HTML templates for rendering the frontend.
- `emotion.py` - Main script for emotion prediction logic and Flask server.
- `emotion_model_1.h5` - Pre-trained model for emotion classification.
- `label_encoder.pkl` - Encodes emotion labels into numerical representations and vice versa.
- `tokenizer.pkl` - Tokenizer to preprocess input text for model predictions.

---

## 🚀 Getting Started

### Prerequisites

Before running the project, ensure the following are installed:

- Python 3.x
- Required libraries: `Flask`, `TensorFlow`, `Keras`, `pickle`, `numpy`, etc.

### Installation

Follow these steps to set up and run the application:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/thilak-r/Text-emotion-reader.git
   cd Text-emotion-reader
   ```

2. **Create and Activate a Virtual Environment**:

   ```bash
   python -m venv venv
   # Activate the virtual environment:
   source venv/bin/activate    # For Linux/macOS
   venv\Scripts\activate       # For Windows
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask Application**:

   ```bash
   python emotion.py
   ```

5. **Access the Application**:

   Open your browser and visit: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 💡 Usage

1. Enter your text in the input field on the web interface.
2. Click on **"Analyze Emotion"**.
3. View the predicted emotion displayed on the screen.

---

## 🧠 Model Details

- **Training Dataset**: The model is trained on a dataset with labeled emotional data.
- **Components**:
  - `emotion_model_1.h5`: The Keras model used for predictions.
  - `label_encoder.pkl`: Converts numerical predictions into emotion labels.
  - `tokenizer.pkl`: Preprocesses text into token sequences for model input.

---


## 🙏 Acknowledgments


- [Dr Agughasi Victor Ikechukwu](https://github.com/Victor-Ikechukwu)


Feel free to contribute, report issues, or suggest features to thilak22005@gmail.com


