from sqlalchemy import Column, Integer, String, Text, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from app.database import Base

class Word(Base):
    __tablename__ = "words"
    
    id = Column(Integer, primary_key=True, index=True)
    word = Column(String(100), unique=True, nullable=False)
    definition = Column(Text)
    difficulty_level = Column(Integer, default=1)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

class PracticeSubmission(Base):
    __tablename__ = "practice_submissions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    word_id = Column(Integer, ForeignKey("words.id"), nullable=False)
    submitted_sentence = Column(Text, nullable=False)
    score = Column(Integer, nullable=False)
    feedback = Column(Text)
    corrected_sentence = Column(Text)
    timestamp = Column(TIMESTAMP(timezone=True), server_default=func.now())
