from bs4 import BeautifulSoup as bs
import requests
import yagmail
import random
from datetime import datetime
from dotenv import load_dotenv
import os

# loads the environment variables
load_dotenv()

username = os.getenv('USERNAMES')
password=os.getenv('PASSWORD')
receiver=os.getenv('receiver')

url = 'https://www.positivityblog.com/comfort-zone-quotes/#more-15686'

response = requests.get(url)
contents = response.content

soup = bs(contents,'html.parser')
soup.find(name='p')
soup.find(name='p').text

quotes = soup.find_all(name='p')
with open('quotes.txt',mode='w',encoding='utf-8') as quote_file:
    for quote in quotes:
        quote_text = quote.text + '\n'
        quote_file.write(quote_text)

yag = yagmail.SMTP(user=username,password=password)

Subject = 'Motivational Quotes to Bless Your Day'

#open file again
with open('quotes.txt',mode='r',encoding='utf-8') as file_read:
    quotelist = file_read.readlines()

quote_for_day = random.choice(quotelist)

today = datetime.now()
weekday = today.weekday()

#sends the mail only on mondays.Which is regarded to as the first day of the week
if weekday == 5:
    yag.send(to=[receiver],subject='Motivational Quote For Your Week',contents=quote_for_day)
