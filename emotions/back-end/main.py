from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from emotion import analyze_emotion
from response_engine import generate_response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    image_bytes = await file.read()

    emotion, confidence, scores = analyze_emotion(image_bytes)
    response = generate_response(emotion)

    return {
        "emotion": emotion,
        "confidence": confidence,
        "scores": scores,
        "response": response
    }
