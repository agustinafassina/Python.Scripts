import boto3

ses_client = boto3.client('ses', region_name='us-east-1',
                           aws_access_key_id='replace_with_your_access_key',
                           aws_secret_access_key='replace_with_your_secret_key')

response = ses_client.send_email(
    Source='notifications@test.us',
    Destination={
        'ToAddresses': [
            'agustina.fassina@gmail.com',
        ],
    },
    Message={
        'Subject': {
            'Data': 'Test Subject',
        },
        'Body': {
            'Text': {
                'Data': 'Test Body',
            },
        },
    }
)