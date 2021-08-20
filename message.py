import os
import random
import schedule
import time
from twilio.rest import Client

class Message():
    def __init__(self, messages_file = "./messages.txt"):
        self.messages_file = messages_file
        self.messages = []

        self._init_tokens()
        self._load_message()

    def _init_tokens(self):
        self.account_id = os.environ.get("TWILIO_ACCOUNT_ID")
        self.auth_token = os.environ.get("TWILIO_AUTH_ID")
        self.client = Client(self.account_id, self.auth_token)

    
    def _load_message(self, data):
        with open(data, 'r') as fl:
            message_list = fl.readlines()
            self.messages = [a[0:len(a)-1] for a in message_list]
            fl.close()

    def send_message(self, phone_number):
        choice = random.randint(0, len(self.messages)-1)
        message_body = self.messages[choice]
        sender = os.environ.get("SENDER_PHONE_NUMBER")
        message = self.client.messages.create(
            body=message_body,
            from_=sender,
            to=phone_number
        )

if __name__ == "__main__":
    message = Message()
    phone = os.environ.get("RECEIVER_PHONE_NUMBER")
    schedule.every().day.at("06:30").do(message.send_message, phone)
