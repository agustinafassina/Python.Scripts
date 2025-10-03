import pymysql

# Replace these with your RDS instance details
host = 'your-rds-endpoint.amazonaws.com'
port = 3306  # Default MySQL port
user = 'your_username'
password = 'your_password'
database = 'your_database_name'

try:
    # Connect to your RDS instance
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=port
    )

    print("Connection successful!")

    # Example: execute a simple query
    with connection.cursor() as cursor:
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        print("Tables in database:", tables)

    # Close the connection
    connection.close()

except Exception as e:
    print("Error connecting to RDS:", e)