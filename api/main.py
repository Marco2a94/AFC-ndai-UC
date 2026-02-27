from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

class Feedback(BaseModel):
    campaign_id: str
    customer_id: str
    comment: str

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )

@app.post("/feedback")
def create_feedback(feedback: Feedback):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO feedback (campaign_id, customer_id, comment, sentiment)
        VALUES (%s, %s, %s, %s)
        """,
        (feedback.campaign_id, feedback.customer_id, feedback.comment, "neutral")
    )

    conn.commit()
    cursor.close()
    conn.close()

    return {"status": "feedback stored"}