from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List, Dict

class WordResponse(BaseModel):
    id: int
    word: str
    definition: str
    difficulty_level: int   # <-- เปลี่ยนเป็น int

    class Config:
        from_attributes = True

class ValidateSentenceRequest(BaseModel):
    word_id: int
    word: str
    difficulty_level: int
    sentence: str

class ValidateSentenceResponse(BaseModel):
    word_id: int
    sentence: str
    score: int
    level: int
    suggestion: Optional[str] = None
    corrected_sentence: Optional[str] = None
    record_id: int

class SummaryResponse(BaseModel):
    total_practices: int
    average_score: float
    total_words_practiced: int
    level_distribution: dict

class HistoryItem(BaseModel):
    id: int
    word: str
    user_sentence: str
    score: float
    feedback: str
    practiced_at: datetime

    class Config:
        from_attributes = True
