import psycopg2

try:
    conn = psycopg2.connect(
        host="nhtsa-recalls-db.cofgcya2a0e7.us-east-1.rds.amazonaws.com",
        port=5432,
        dbname="postgres",
        user="postgres",
        password="rickyKUC17$"
    )
    print("Connected successfully!")
    conn.close()
except Exception as e:
    print("Connection failed:", e)