from twilio.rest import Client
from email_swiss import retrieve_messages
import os

def retrieve():
  account_sid = os.getenv('ACC_SID')
  auth_token = os.getenv('AUTH_TOKEN')
  client = Client(account_sid, auth_token)

  message_quant=int(input("Enter number of last recent emails required?: "))

  for messages in retrieve_messages(message_quant):
    message_body=f"From: {messages[2]}\nDate: {messages[0]}\nSubject: {messages[1]}"
    message = client.messages.create(
      from_='whatsapp:+14155238886',
      body=message_body,
      to='whatsapp:+919074570496'
    )


