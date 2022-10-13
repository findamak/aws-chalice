import os
from twilio.rest import Client

# Twilio Config
ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('AUTH_TOKEN')
FROM_NUMBER = os.environ.get('FROM_NUMBER')
TO_NUMBER = os.environ.get('TO_NUMBER')

# Create a twilio client using account_sid and auth token
tw_client = Client(ACCOUNT_SID, AUTH_TOKEN)


def send(payload_params=None):
    """ send sms to the specified number """
    msg = tw_client.messages.create(
        from_=FROM_NUMBER,
        body=payload_params['msg'],
        to=TO_NUMBER)

    if msg.sid:
        return msg