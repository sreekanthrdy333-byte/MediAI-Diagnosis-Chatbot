from ultralytics import YOLO
import cv2
import numpy as np
import os

class ModelRegistry:
      def __init__(self):
                self.models = {"Chest X-ray": "yolov8n.pt", "Eye Fundus": "yolov8n.pt", "Bone X-ray": "yolov8n.pt", "Plant Leaf": "yolov8n.pt"}
                self.loaded_models = {}

      def get_model(self, category):
                if category not in self.models: return None
                          if category not in self.loaded_models:
                                        try: self.loaded_models[category] = YOLO(self.models[category])
                                                      except: return None
                                                                return self.loaded_models[category]

            def detect(self, category, image):
                      model = self.get_model(category)
                      if not model: return None, []
                                results = model(image)
        detections = []
        for r in results:
                      for box in r.boxes:
                                        detections.append({"class": model.names[int(box.cls)], "confidence": float(box.conf), "bbox": [float(x) for x in box.xyxy[0]]})
                                return results[0].plot(), detections

class MockDetector:
      def __init__(self, gemini_engine): self.gemini = gemini_engine
            def simulate_detection(self, category, image):
                      return [{"class": "Pneumonia" if "Chest" in category else "Glaucoma", "confidence": 0.89, "bbox": [50, 50, 200, 200]}]
