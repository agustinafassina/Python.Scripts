import jwt
import datetime

# Secret key for encoding the JWT
secret_key = '9A..................C'

# Payload data for the JWT
payload = {
    'sub': 'agus_fassina',               # UserId
    'nombre': 'Agus Fassina',                # UserName
    'iat': datetime.datetime.now(),     # Print date
    'exp': datetime.datetime.now() + datetime.timedelta(hours=1)  # Expiration time (1 hour from now)
}

# Jwt generate token
token = jwt.encode(payload, secret_key, algorithm='HS256')

# Print token in  the console
print(token)