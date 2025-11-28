#pip install twilio (First)
from twilio.rest import Client
ACCOUNT_SID = "ACfbcc218b2"
AUTH_TOKEN = "1c27f96761e21c4952cad668e4b4fbdf" 
TWILIO_NUMBER = "      "
RECIVER_NUMBER = ""
Client = Client.message.create(
    body = " Hello i am Ravi ",
    from = TWILIO_NUMBER,
to=RECEIVER_NUMBER
)
print("SMS sent successfully Message SID:", message.sid)
