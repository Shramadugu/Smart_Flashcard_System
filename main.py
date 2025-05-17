"""
FastAPI app for a Smart Flashcard System

Features:
- POST /flashcard: Add a flashcard with automatic subject inference based on the question.
- GET /get-subject: Retrieve a mixed batch of flashcards from different subjects for a student.
"""

from fastapi import FastAPI, Query
from pydantic import BaseModel
from subject_classifier import detect_subject         
from storage import save_flashcard, get_flashcards_by_mixed_subjects  

app = FastAPI()

@app.get("/")
def read_root():
    """
    Simple root endpoint to check if API is running.
    """
    return {"message": "Hello from Flashcard API"}


class Flashcard(BaseModel):
    """
    Schema to validate flashcard input data.
    """
    student_id: str
    question: str
    answer: str


@app.post("/flashcard")
def add_flashcard(card: Flashcard):
    """
    Add a flashcard with inferred subject.
    Steps:
    - Infer subject using question text.
    - Save flashcard details with subject.
    - Return confirmation with detected subject.
    """
    subject = detect_subject(card.question)

    flashcard_data = {
        "student_id": card.student_id,
        "question": card.question,
        "answer": card.answer,
        "subject": subject
    }

    save_flashcard(flashcard_data)

    return {"message": "Flashcard added successfully", "subject": subject}


@app.get("/get-subject")
def get_flashcards(student_id: str = Query(...), limit: int = Query(5)):
    """
    Retrieve up to `limit` flashcards for a student.
    - The flashcards returned are mixed from different subjects.
    - This helps the student study varied topics in one batch.
    """
    flashcards = get_flashcards_by_mixed_subjects(student_id, limit)
    return flashcards
