# model.py
import cv2
import numpy as np
from fer import FER

# Initialize the FER model
emotion_detector = FER(mtcnn=True)

def analyze_emotion(image_path: str) -> dict:
    """
    Analyze emotions in a given image.
    Returns the top emotion and full emotion scores.
    """
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Image not found: {image_path}")
    
    # Detect emotions
    results = emotion_detector.detect_emotions(img)
    if not results:
        return {"error": "No face detected"}

    emotions = results[0]["emotions"]
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "dominant_emotion": dominant_emotion,
        "scores": emotions
    }

if __name__ == "__main__":
    # Quick test
    test_image = "data/test_image.jpg"  # Replace with any test image
    print(analyze_emotion(test_image))
if __name__ == "__main__":
    from fer import FER
    import cv2

    detector = FER(mtcnn=True)
    img = cv2.imread("data/test_image.jpg")
    result = detector.detect_emotions(img)
    print(result)
from fer import FER
import cv2

def detect_emotion(image_path):
    detector = FER(mtcnn=True)
    img = cv2.imread(image_path)
    if img is None:
        return None
    result = detector.detect_emotions(img)
    if not result:
        return None
    return {
        "dominant_emotion": detector.top_emotion(img)[0],
        "scores": result[0]["emotions"]
    }


