# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC53fce67a234c1a0aa49e7eee48d2e984'
auth_token = '1e382fca3d6a188b04719a6878984f7a'
client = Client(account_sid, auth_token)

to_numbers = ['+15203016608', '+18586667700', '+19375225522']

for number in to_numbers:
    message = client.messages \
                    .create(
                        body="ALERT: Your trusted contact JARROD MANGUIAT has been arrested.",
                        from_='+12674940751',
                        to=number
                    )

    print(message.sid)
