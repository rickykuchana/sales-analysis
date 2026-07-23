from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date
import json
import psycopg2

def get_connection():
    return psycopg2.connect(
        host="nhtsa-recalls-db.cofgcya2a0e7.us-east-1.rds.amazonaws.com",
        port=5432,
        dbname="postgres",
        user="postgres",
        password="rickyKUC17$"
    )

with open("recalls_clean.json") as f:
    RECALLS = json.load(f)

app = FastAPI()


class Recall(BaseModel):
    """The shape a valid recall must have. Pydantic rejects anything that doesn't match."""
    NHTSACampaignNumber: str
    Manufacturer: str
    Component: str
    Summary: str
    Make: str
    Model: str
    ModelYear: str
    ReportReceivedDate: date = date.today()


@app.get("/health")
def health():
    """Liveness check so monitoring can confirm the service is up."""
    return {"status": "ok"}


@app.get("/recalls/{campaign_number}")
def get_recall(campaign_number: str):
    """Return one recall by its NHTSA campaign number."""
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM recalls WHERE campaign_number = %s", (campaign_number,))
    row = cur.fetchone()

    cur.close()
    conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="Recall not found")

    return {
        "campaign_number": row[0],
        "make": row[1],
        "model": row[2],
        "model_year": row[3],
        "report_received_date": row[4],
        "summary": row[5]
    }


@app.post("/ingest")
def ingest(recall: Recall):
    """Accept a new recall record and add it to the database."""
    conn = get_connection()
    cur = conn.cursor()

    insert_query = """
    INSERT INTO recalls (campaign_number, make, model, model_year, report_received_date, summary)
    VALUES (%s, %s, %s, %s, %s, %s)
    ON CONFLICT (campaign_number) DO NOTHING;
    """

    cur.execute(insert_query, (
        recall.NHTSACampaignNumber,
        recall.Make,
        recall.Model,
        recall.ModelYear,
        recall.ReportReceivedDate,
        recall.Summary
    ))

    conn.commit()
    cur.close()
    conn.close()

    return {"status": "added", "campaign_number": recall.NHTSACampaignNumber}