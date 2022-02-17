from datetime import datetime
import yagmail
import pandas
import dateparser
from dotenv import load_dotenv
import os

# loads the environment variables
load_dotenv()

username = os.getenv('USERNAMES')
password=os.getenv('PASSWORD')
receiver=os.getenv('receiver')
csvfile=os.getenv('csv_file')
letterfile=os.getenv('letterfile')

# creates a dataframe
email_details = pandas.read_csv(csvfile)

today = datetime.now()
ptoday = (today.month,today.day)

# list contains multiple tuples that hold month and day of bday
bdaylist = []
for i in email_details['date']:
    bdate = dateparser.parse(i)
    bdetail = (bdate.month,bdate.day)
    bdaylist.append(bdetail)

# a dictionary where the tuple is the key
bdict = {}
for i,j in email_details.iterrows():
    a = list(j)
    k = a.pop()
    bdict[bdaylist[i]] = a

if ptoday in bdict:
    name = bdict[ptoday][0]
    email = bdict[ptoday][1]

with open(letterfile,mode='r+') as file:
    edit = file.read()
    edit = edit.replace('[Name]',name)

topic = 'Birthday Message'

# Writing a yagmail object
yag = yagmail.SMTP(user=username,password=password)
yag.send(to=[receiver],subject=topic,contents=edit)
