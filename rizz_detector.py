from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from modal import Image, Mount, Stub, asgi_app

stub = Stub("rizz-detector")

app = FastAPI()

class TranscriptSegment(BaseModel):
    text: str
    speaker: str
    speaker_id: int
    is_user: bool
    start: float
    end: float

class RizzDetectorData(BaseModel):
    session_id: str
    segments: List[TranscriptSegment]

def analyze_rizz(segments):
    rizz_score = 0
    rizz_keywords = ['confident', 'charming', 'smooth', 'flirty', 'witty']
    
    for segment in segments:
        for keyword in rizz_keywords:
            if keyword in segment.text.lower():
                rizz_score += 1
    
    rizz_score = min(rizz_score, 10)
    
    return f"rizz level detected: {rizz_score}/10"

@stub.function()
@asgi_app()
def fastapi_app():
    @app.post('/rizz-detector')
    def rizz_detector_endpoint(data: RizzDetectorData):
        return {'message': analyze_rizz(data.segments)}
    
    return app

if __name__ == "__main__":
    stub.serve()