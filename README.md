# MediAI-Diagnosis-Chatbot
## AI-Powered Multi-Specialist Medical Diagnosis Chatbot

### Project Overview
MediAI is an AI-driven Medical Diagnosis Chatbot that utilizes Convolutional Neural Networks (CNNs), specifically YOLOv8, for detecting medical conditions such as eye diseases, lung cancer, fractures, and agricultural plant diseases. The chatbot is interactive and provides possible diagnoses and recommendations using the Gemini API.

### Key Features
- **CNN-Based Disease Detection**: Supports multiple models for Eye, Lung, Bone, and Agriculture.
- **Intelligent Routing**: Automatically detects the type of image and routes it to the correct specialized model.
- **LLM-Powered Insights**: Uses Gemini API to provide contextual medical advice and explanations.
- **Streamlit Web UI**: A high-end, dark-themed glassmorphic interface for a smooth user experience.
- **Accessibility**: Includes Text-to-Speech (TTS), Speech-to-Text (STT), and multilingual support.

### Tech Stack
- **Framework**: Streamlit
- **Deep Learning**: YOLOv8 (Ultralytics)
- **LLM**: Google Gemini API
- **Image Processing**: OpenCV, PIL
- **Voice**: gTTS, Streamlit Mic Recorder

### Setup & Installation
1. Clone the repository
2. Install dependencies: `pip install streamlit ultralytics google-generativeai pillow opencv-python gtts streamlit-mic-recorder`
3. Run the app: `streamlit run app.py`

---
*Developed for the AI-Powered Medical Diagnosis Chatbot Hackathon.*
