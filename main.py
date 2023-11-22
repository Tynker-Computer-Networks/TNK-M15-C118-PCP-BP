import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SecretSanta():
    def __init__(self):
        super().__init__()
        
   
    def send_email(self):
        try:
            sender_email = input("Enter Sender Email\n")
            password = input("Enter Sender Password\n")
            recipient_name = input("Enter Recipient Name\n")
            recipient_email = input("Enter Recipient Email\n")
            wishlist = input("Enter Comma Seperated Wihslist\n")
            assigned_to = input("Enter Participent Name to assign\n")

            # Send mail using SMTP server
            


        except Exception as e:
            print("Error",f"An error occurred:{str(e)}")



def main():
    app = SecretSanta()
    app.send_email()


if __name__ == "__main__":
    main()
