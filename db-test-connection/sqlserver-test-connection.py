import pyodbc

# Replace with your SQL Server details
server = ''
database = ''
username = 'admin'
password = ''

# Connection string
connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"

try:
    # Connect to SQL Server
    with pyodbc.connect(connection_string, timeout=5) as conn:
        print("Connection successful!")

        # Optionally, execute a simple query
        with conn.cursor() as cursor:
            cursor.execute("SELECT @@VERSION;")
            version_info = cursor.fetchone()
            print("SQL Server version:", version_info[0])

except Exception as e:
    print("Error connecting to SQL Server:", e)