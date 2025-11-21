from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import PracticeSubmission
from app.utils import mock_ai_validation
from app.schemas import ValidateSentenceRequest, ValidateSentenceResponse

router = APIRouter()

@router.post("/validate-sentence", response_model=ValidateSentenceResponse)
def validate_sentence(data: ValidateSentenceRequest, db: Session = Depends(get_db)):

    try:
        # เรียก mock AI
        result = mock_ai_validation(
            data.sentence,
            data.word,
            data.difficulty_level
        )

        # ✅ แปลง score เป็น int ทั้ง DB และ response
        score = int(round(result.get("score", 0)))

        # Save to database
        new_record = PracticeSubmission(
            user_id=1,
            word_id=data.word_id,
            submitted_sentence=data.sentence,
            score=score,
            feedback=result.get("suggestion"),
            corrected_sentence=result.get("corrected_sentence")
        )

        db.add(new_record)
        db.commit()
        db.refresh(new_record)

        # ส่ง response
        return ValidateSentenceResponse(
            word_id=data.word_id,
            sentence=data.sentence,
            score=score,
            level=result.get("level", data.difficulty_level),
            suggestion=result.get("suggestion"),
            corrected_sentence=result.get("corrected_sentence"),
            record_id=new_record.id
        )

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
