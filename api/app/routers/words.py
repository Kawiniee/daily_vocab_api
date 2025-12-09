from fastapi import APIRouter, HTTPException
import random

router = APIRouter()

# ใช้ difficulty_level เป็น int: 1=Beginner, 2=Intermediate, 3=Advanced
words = [
    {"id": 1, "word": "Ephemeral", "definition": "Lasting for a very short time.", "difficulty_level": 3},
    {"id": 2, "word": "Ubiquitous", "definition": "Present, appearing, or found everywhere.", "difficulty_level": 2},
    {"id": 3, "word": "Mellifluous", "definition": "(Of a voice or words) sweet or musical; pleasant to hear.", "difficulty_level": 3},
    {"id": 4, "word": "Serendipity", "definition": "The occurrence and development of events by chance in a happy or beneficial way.", "difficulty_level": 2},
    {"id": 5, "word": "Happy", "definition": "Feeling or showing pleasure or contentment.", "difficulty_level": 1},
    {"id": 6, "word": "Run", "definition": "Move at a speed faster than a walk.", "difficulty_level": 1}
]

@router.get("/word")
def get_random_word():
    if not words:
        raise HTTPException(status_code=404, detail="No words available")
    return random.choice(words)
