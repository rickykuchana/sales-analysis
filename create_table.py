import psycopg2

conn = psycopg2.connect(
    host="nhtsa-recalls-db.cofgcya2a0e7.us-east-1.rds.amazonaws.com",
    port=5432,
    dbname="postgres",
    user="postgres",
    password="rickyKUC17$"
)

cur = conn.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS recalls (
    campaign_number VARCHAR(20) PRIMARY KEY,
    make VARCHAR(50),
    model VARCHAR(50),
    model_year INTEGER,
    report_received_date DATE,
    summary TEXT
);
"""

cur.execute(create_table_query)
conn.commit()
cur.close()
conn.close()

print("Table created!")