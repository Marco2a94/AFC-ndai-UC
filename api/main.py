from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
import os
from dotenv import load_dotenv
from textblob import TextBlob

from datetime import date

load_dotenv()

app = FastAPI(
    title="AFC Feedback API",
    description="REST API to collect campaign feedback and perform sentiment analysis",
    version="1.0.0"
)

class Feedback(BaseModel):
    campaign_id: str
    username: str
    comment: str
    feedback_date: date

def get_connection():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        dbname=os.getenv("POSTGRES_DB"),
    )

def analyze_sentiment(text: str) -> str:
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/feedback")
def create_feedback(feedback: Feedback):
    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        sentiment = analyze_sentiment(feedback.comment)

        cursor.execute(
            """
            INSERT INTO feedback
            (campaign_id, username, comment, sentiment, feedback_date)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                feedback.campaign_id,
                feedback.username,
                feedback.comment,
                sentiment,
                feedback.feedback_date
            )
        )

        conn.commit()

        return {
            "status": "feedback stored",
            "sentiment": sentiment
        }

    except Exception as e:
        return {"error": str(e)}

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()