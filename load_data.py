import psycopg2
import json
from datetime import datetime

conn = psycopg2.connect(
    host="nhtsa-recalls-db.cofgcya2a0e7.us-east-1.rds.amazonaws.com",
    port=5432,
    dbname="postgres",
    user="postgres",
    password="rickyKUC17$"
)

cur = conn.cursor()

with open("recalls_clean.json") as f:
    recalls = json.load(f)

insert_query = """
INSERT INTO recalls (campaign_number, make, model, model_year, report_received_date, summary)
VALUES (%s, %s, %s, %s, %s, %s)
ON CONFLICT (campaign_number) DO NOTHING;
"""

for recall in recalls:
    report_date = datetime.fromtimestamp(recall["ReportReceivedDate"] / 1000).date()

    cur.execute(insert_query, (
        recall["NHTSACampaignNumber"],
        recall["Make"],
        recall["Model"],
        recall["ModelYear"],
        report_date,
        recall["Summary"]
    ))

conn.commit()
cur.close()
conn.close()

print(f"Loaded {len(recalls)} recalls into the database.")
