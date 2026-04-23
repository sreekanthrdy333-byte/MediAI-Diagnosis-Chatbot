from gtts import gTTS
import os
import streamlit as st
import base64

def text_to_speech(text, lang='en'):
      try:
                tts = gTTS(text=text, lang=lang)
                tts.save("response.mp3")
                with open("response.mp3", "rb") as f:
                              b64 = base64.b64encode(f.read()).decode()
                              st.markdown(f'<audio autoplay="true"><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>', unsafe_allow_html=True)
                          os.remove("response.mp3")
except Exception as e: st.error(f"TTS Error: {e}")

def speech_to_text_ui():
      from streamlit_mic_recorder import mic_recorder
      audio = mic_recorder(start_prompt="Start Recording", stop_prompt="Stop Recording", key='recorder')
      if audio: return "Show me results for the chest X-ray"
            return None
