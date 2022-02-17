import os
from dotenv import load_dotenv
from twilio.rest import Client

import requests

load_dotenv()

# Get the message from the twilio api
account_sid = os.getenv('Account_Sid')
auth_token = os.getenv('Auth_Token')
client = Client(account_sid, auth_token)
fromPhoneNo = os.getenv('FromPhoneNo')
toPhoneNo = os.getenv('ToPhoneNo')

def send_message(body):
    client.messages.create(
                        body=body,
                        from_=fromPhoneNo,
                        to=toPhoneNo
                    )
    

# Get the response from the openweather api
lat = -22.908333
lon = -43.196388
appid = os.getenv('AppId')
exclude = "current,minutely,daily"
url = "https://api.openweathermap.org/data/2.5/onecall"
param = {'lat':lat,'lon':lon,"appid":appid,"exclude":exclude}
response = requests.get(url,params=param)

# Working with the response
data = response.json()
weather_id = [data['hourly'][i]['weather'][0]['id'] for i in range(5,22)]
for weather in weather_id:
    if weather < 700:
        if weather in range(200,233):
            text = "There is a thunderstorm. Stay at home!"
            send_message(text)
            break
        elif weather in range(600,623):
            text = "There is going to be snowfall!"
            send_message(text)
            break
        elif weather in range(500,532):
            text = 'It will rain. Bring an umbrella!'
            send_message(text)
            break
        elif weather in range(300,322):
            text = "There will be a drizzle. Bring an umbrella!"
            send_message(text)
            break