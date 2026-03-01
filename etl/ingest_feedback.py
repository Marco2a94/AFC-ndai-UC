import json
import sys
from textblob import TextBlob
from etl.db_utils import get_connection


def analyze_sentiment(text: str) -> str:
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"


def ingest_feedback(json_path):
    print("Reading JSON file...")

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    conn = get_connection()
    cursor = conn.cursor()

    print("Cleaning existing feedback data...")

    print("Inserting feedback records...")

    for entry in data:
        sentiment = analyze_sentiment(entry["comment"])

        cursor.execute(
            """
            INSERT INTO feedback
            (campaign_id, username, comment, sentiment, feedback_date)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                entry["campaign_id"],
                entry["username"],
                entry["comment"],
                sentiment,
                entry["feedback_date"]
            )
        )

    conn.commit()
    cursor.close()
    conn.close()

    print("Feedback batch ETL completed successfully.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ingest_feedback.py <path_to_json>")
        sys.exit(1)

    ingest_feedback(sys.argv[1])