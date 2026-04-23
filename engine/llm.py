import google.generativeai as genai
import PIL.Image
from config import GEMINI_API_KEY

class GeminiMedical:
      def __init__(self):
                genai.configure(api_key=GEMINI_API_KEY)
                self.model = genai.GenerativeModel('gemini-1.5-flash')
                self.vision_model = genai.GenerativeModel('gemini-1.5-flash')

      def get_medical_insights(self, detection_results, context_image=None):
                prompt = f"You are a Multi-Super-Specialist Medical AI. Detection Results: {detection_results}\nBased on these findings, provide: 1. Possible causes 2. Basic medical advice 3. When to seek consultation."
                if context_image: response = self.vision_model.generate_content([prompt, context_image])
else: response = self.model.generate_content(prompt)
        return response.text

    def chat_response(self, user_query, history=[]):
              chat = self.model.start_chat(history=history)
              response = chat.send_message(user_query)
              return response.text

    def classify_image_type(self, image):
              prompt = "Analyze this image and classify it into: Chest X-ray, Eye Fundus, Bone X-ray, Plant Leaf, Other. Return ONLY the category name."
              response = self.vision_model.generate_content([prompt, image])
              return response.text.strip()
      
