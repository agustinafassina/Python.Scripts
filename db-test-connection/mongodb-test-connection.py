from pymongo import MongoClient

# Replace these values with your instance details
host = 'host-replace'
port = 27017  # or your MongoDB port
database_name = 'agus-test'

# Connection URI
# with user and password
# uri = f"mongodb://{username}:{password}@{host}:{port}/{database_name}"
uri = f"mongodb://{host}:{port}/{database_name}"
try:
    # Create a MongoDB client
    client = MongoClient(uri)

    # Test the connection
    # List available databases
    print("Successfully connected. Available databases:")
    print(client.list_database_names())

    # Select the database
    db = client[database_name]

    # Example: list collections within the database
    print("Collections in the database:")
    print(db.list_collection_names())

except Exception as e:
    print("Error connecting to MongoDB:", e)