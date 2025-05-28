from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Think Like a Game Designer (TLAGD)")

class CritiqueRequest(BaseModel):
    prompt: str
    persona: Optional[str] = None

class CritiqueResponse(BaseModel):
    persona: str
    feedback: str

# Placeholder: list of available personas
def get_personas() -> List[str]:
    return [
        "Richard Garfield",
        "Sid Meier",
        "Yoko Taro",
        "Mark Rosewater"
    ]

@app.get("/personas", response_model=List[str])
def list_personas():
    return get_personas()

@app.post("/critique", response_model=CritiqueResponse)
def critique(request: CritiqueRequest):
    # Placeholder logic: echo prompt with persona flavor
    persona = request.persona or "Richard Garfield"
    feedback = f"[{persona}]: This is where your design feedback will appear for: {request.prompt}"
    return CritiqueResponse(persona=persona, feedback=feedback)
