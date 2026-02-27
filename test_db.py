import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="afc_db",
    user="afc_user",
    password="afc_password"
)

print("Connected to PostgreSQL!")
conn.close()