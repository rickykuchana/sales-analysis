from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

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


@app.get("/health")
def health():
    """Liveness check so monitoring can confirm the service is up."""
    return {"status": "ok"}


@app.get("/recalls/{campaign_number}")
def get_recall(campaign_number: str):
    """Return one recall by its NHTSA campaign number."""
    for recall in RECALLS:
        if recall["NHTSACampaignNumber"] == campaign_number:
            return recall
    raise HTTPException(status_code=404, detail="Recall not found")


@app.post("/ingest")
def ingest(recall: Recall):
    """Accept a new recall record and add it to the store."""
    RECALLS.append(recall.model_dump())
    return {"status": "added", "campaign_number": recall.NHTSACampaignNumber}