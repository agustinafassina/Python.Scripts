import psycopg2
from psycopg2 import sql

# Replace these with your PostgreSQL database details
host = ''
port = 5432  # Port by default for PostgreSQL
database = ''
user = ''
password = ''

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )
    print("Connection successful!")

    # Create a cursor
    cur = conn.cursor()

    # Execute a query to list all tables in public schema
    cur.execute("""
        SELECT table_name FROM information_schema.tables
        WHERE table_schema='public';
    """)

    tables = cur.fetchall()
    print("Tables in the database:")
    for table in tables:
        print(table[0])

    # Close cursor and connection
    cur.close()
    conn.close()

except Exception as e:
    print("Error connecting to PostgreSQL:", e)