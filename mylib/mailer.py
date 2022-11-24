import smtplib

class Mailer:

    """
    This script initiaties the email alert function.

    """
    def __init__(self):
        # WRITE THE SENDER'S email address here:
        self.EMAIL = ""
        #the password for the email address || Create an app inside your google acount and write tha google generated password here:
        self.PASS = ""

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
