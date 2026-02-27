from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
import os
from dotenv import load_dotenv
from textblob import TextBlob

load_dotenv()

app = FastAPI()

class Feedback(BaseModel):
    campaign_id: str
    username: str
    comment: str
    feedback_date: str

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

@app.post("/feedback")
def create_feedback(feedback: Feedback):
    conn = get_connection()
    cursor = conn.cursor()

    sentiment = analyze_sentiment(feedback.comment)

    cursor.execute(
        """
        INSERT INTO feedback (campaign_id, username, comment, sentiment, feedback_date)
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
    cursor.close()
    conn.close()

    return {
        "status": "feedback stored",
        "sentiment": sentiment
    }