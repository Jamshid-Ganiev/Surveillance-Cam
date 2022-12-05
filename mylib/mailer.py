import smtplib
from twilio.rest import Client
import config

class Mailer:

    """
    This script initiaties the email alert function.

    """
    def __init__(self):
        # sender's email address
        self.EMAIL = ""
        # create an app in you google account and enter the password of the app here 
        self.PASS = ""

    def send(self, mail_list):
        for worker_email in mail_list:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls(),
                connection.login(user=self.EMAIL, password=self.PASS),
                text = f'[OVER {config.LIMIT}]People Limit exceeded in the building!',
                connection.sendmail(
                    from_addr=self.EMAIL,
                    to_addrs=worker_email,
                    msg = "Subject:'ALERT! ||by GIGA TEAM':.\n\n {}.".format(text)
                )
            
class SMSMailer:
    def __init__(self):
        # the given number in your twilio account
        self.number =''
        self.account_sid = ""
        self.auth_token = ""
    
    def send(self, phone_number):

        client = Client(self.account_sid, self.auth_token)

        message = client.messages.create(
            body=f"[Over {config.LIMIT}]People Limit exceeded in the building!",
            from_=self.number,
            to=phone_number
        )

        print(message.status)
