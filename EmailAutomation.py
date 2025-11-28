import smtplib
import ssl
from email.message import EmailMessage
EMAIL = "rxxxxxzzz@gmail.com"
APP_PASSWORD = "NNNJ"
RECEIVER = "ryyyyzzz@gmail.com"
msg = EmailMessage()
msg["From"] = EMAIL
msg["To"] = RECEIVER
msg["Subject"] = "Hello from Python!"
msg.set_content("This email sent using Python .")
context = ssl.create_default_context()
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(EMAIL, APP_PASSWORD)
        server.send_message(msg)
        print("Email sent successfully!")
except Exception as e:
    print(f"X Error: {e}")
