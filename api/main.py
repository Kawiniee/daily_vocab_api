from fastapi import FastAPI
from app.routers import words, validate_sentence
from app.database import init_db  # ✅ import init_db

app = FastAPI(
    title="Vocabulary Practice API",
    version="1.0.0",
    description="API for vocabulary practice and learning"
)

# ✅ สร้าง table ก่อน router ทำงาน
init_db()

# Include routers
app.include_router(words.router, prefix="/api", tags=["words"])
app.include_router(validate_sentence.router, prefix="/api", tags=["validate"])

@app.get("/")
def read_root():
    return {
        "message": "Vocabulary Practice API",
        "version": "1.0.0",
        "endpoints": {
            "random_word": "/api/word",
            "validate": "/api/validate-sentence",
            "summary": "/api/summary",
            "history": "/api/history"
        }
    }
