import redis

# Replace with your Redis server details
host = ''  # por ejemplo, 'localhost' o la IP del servidor Redis
port = 6379  # puerto por defecto de Redis
password = ''  # si tu Redis requiere autenticación, sino puedes dejarlo como None

try:
    # Connect to Redis
    r = redis.Redis(host=host, port=port, password=password, socket_timeout=5)

    # Test connection
    if r.ping():
        print("Connection successful!")

        # Set a test key (optional)
        r.set('test_key', 'hello redis!')

        # List all keys
        print("Listing all keys in Redis:")
        cursor = 0
        keys = []
        while True:
            cursor, data = r.scan(cursor=cursor, count=100)
            keys.extend(data)
            if cursor == 0:
                break

        # Print keys
        for key in keys:
            print(key.decode())

except Exception as e:
    print("Error connecting to Redis:", e)