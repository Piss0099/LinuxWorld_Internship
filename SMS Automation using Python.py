#pip install twilio (First)
from twilio.rest import Client
ACCOUNT_SID = "ENTER SID NUBER FROM OFFICIAL WEB PORTAL"
AUTH_TOKEN = "ENTER TOKEN NUBER" 
TWILIO_NUMBER = "  ENTER TWILIO NUMBER WHICH YOU GET FROM WEBSITE    "
RECIVER_NUMBER = "ENTER WHERE TO SEND SMS"
Client = Client.message.create(
    body = " Hello I am Ravi ",
    from = TWILIO_NUMBER,
to=RECEIVER_NUMBER
)
print("SMS sent successfully Message SID:", message.sid)
