import smtplib

class Mailer:

    """
    This script initiaties the email alert function.

    """
    def __init__(self):
        self.EMAIL = "jamesganiev227@gmail.com"
        self.PASS = "wzcbduietbgbfwne"

    def send(self, mail):


        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.EMAIL, password=self.PASS)
            text = 'People Limit exceeded in the building!',
            connection.sendmail(
                from_addr=self.EMAIL,
                to_addrs=mail,
                msg = "Subject:'ALERT! ||by GIGA TEAM':.\n\n {}.".format(text)
            )