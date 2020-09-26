import os
import random
import schedule
import time
from twilio.rest import Client

class Message():
    def __init__(self, messages_file = "messages.txt"):
        self.messages_file = messages_file
        self.messages = []
        
        self.init_tokens()
        self.load_message()

    def init_tokens(self):
        self.account_id = os.environ.get("TWILIO_ACCOUNT_ID")
        self.auth_token = os.environ.get("TWILIO_AUTH_ID")
        self.client = Client(self.account_id, self.auth_token)

    
    def load_message(data=self.messages_file):
        with open(data, 'r') as fl:
            message_list = fl.readlines()
            self.messages = [a[0:len(a)-1] for a in message_list]
            fl.close()

    def send_message(phone_number):
        choice = random.randint(0, len(self.messages)-1)
        message_body = self.messages[choice]
        sender = '+4917674729258'
        message = self.client.messages.create(
            body = message_body,
            from = sender,
            to = phone_number
        )

if __name__ = "__main__"
    message = Message()
    phone = '+491628996477'
    schedule.every().day.at("06:30").do(message.send_message, phone)
