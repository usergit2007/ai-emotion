import cv2
import numpy as np
from deepface import DeepFace

EMOTIONS = ["angry", "happy", "sad", "surprise", "neutral"]

def analyze_emotion(image_bytes: bytes):
    np_img = np.frombuffer(image_bytes, np.uint8)
    frame = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    result = DeepFace.analyze(
        frame,
        actions=["emotion"],
        enforce_detection=False
    )

    emotions = result[0]["emotion"]

    scores = {e: float(emotions.get(e, 0.0)) for e in EMOTIONS}
    top_emotion = max(scores, key=scores.get)
    confidence = int(scores[top_emotion])

    return top_emotion, confidence, scores
