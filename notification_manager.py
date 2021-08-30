# This class is responsible for sending notifications with the deal flight details.
from twilio.rest import Client
from pprint import pprint
import smtplib

MY_EMAIL = "onlyyedpad@gmail.com"
MY_PASSWORD = "vcxz4321"

account_sid = "AC95feb8df6b4e12565a937cf36b40e701"
auth_token = "aaf3a412bf3c5403c941e966256818e2"


class NotificationManager:

    def send_sms(self, message):
        # client = Client(account_sid, auth_token)
        # message = client.messages \
        #     .create(
        #     body=message,
        #     from_="+16466813760",
        #     to="+66922807322"
        # )
        # print(message.status)
        pprint(message)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )


