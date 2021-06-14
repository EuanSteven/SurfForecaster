# main.py for python-surf-forecast
# Author: Xioto
# Last updated: 14/06/2021
# Version 1.3
# Latest Change: Added Loading Screen & Small Patches
# Licensed under the MIT License

import requests # for API requests
import datetime # for finding date
import warnings # for ignoring SyntaxWarnings
import json # for caching API response
import smtplib # for sending emails
import sys # for printing dots
import discord_webhook # for discord webhook
from discord_webhook import DiscordWebhook # renaming
from email.mime.multipart import MIMEMultipart # for adding HTML email support (coming soon...)
from email.mime.text import MIMEText # for sending Basic Text in emails
from time import sleep # see sys comment


print ('''
██████╗░██╗░░░██╗░░░░░░░██████╗██╗░░░██╗██████╗░███████╗
██╔══██╗╚██╗░██╔╝░░░░░░██╔════╝██║░░░██║██╔══██╗██╔════╝
██████╔╝░╚████╔╝░█████╗╚█████╗░██║░░░██║██████╔╝█████╗░░
██╔═══╝░░░╚██╔╝░░╚════╝░╚═══██╗██║░░░██║██╔══██╗██╔══╝░░
██║░░░░░░░░██║░░░░░░░░░██████╔╝╚██████╔╝██║░░██║██║░░░░░
╚═╝░░░░░░░░╚═╝░░░░░░░░░╚═════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░

''')


print("""\
ＴＨＡＮＫ ＹＯＵ ＦＯＲ  ＵＳＩＮＧ ＴＨＥ ＰＹＴＨＯＮ－ＳＵＲＦ－ＦＯＲＥＣＡＳＴ
               """)

print("Checking for updates")

words = "......................."
for char in words:
    sleep(0.3)
    sys.stdout.write(char)
    sys.stdout.flush()


version = 1.3

if version == 1.2:
  print('''
You are up to date!''')

else :
    print("You are Out-of-Date! Please update at https://github.com/Xioto/python-surf-forecast/releases/")

cache_file = 'response.json'
data = []

def fxn():
    warnings.warn("deprecated", DeprecationWarning)

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fxn()

weekno = datetime.datetime.today().weekday() # finds current date
if weekno < 5: # if today is a weekday
    pass
else: #if today is a weekend
    print("Attempting to load " + cache_file)
    with open(cache_file, 'r') as f: # opens cache_file 
        data = json.load(f)
    response = requests.get( # sends request to API
        'https://api.stormglass.io/v2/weather/point',
          params={
        'lat': your-lat-for-surf-location, # add your location here
        'lng': your-long-for-surf-location,
        'params': 'waveHeight', 
      },
      headers={
        'Authorization': 'auth-key' # read docs on how to get an API key
      }
      )
    data = response.json()
    print("Writing Json cache to " + cache_file)
    with open(cache_file, 'w') as f:
        json.dump(data,f) # dumps response from API in response.json (cache_file)

    sorted(data, key=lambda i:i['hours']) #sorts cache_file
    print([0])
    if 'waveHeight' in [0] and 'dwd' in [0]['waveHeight'] and [0]['waveHeight']['dwd'] >= 2.00:
        print('Found') # if a waveHeight above 2.00 is found then send email

    mail_content = '''
    "MAIL_CONTENT"
    ''' # content for email
    sender_address = 'your-gmail-address' # see docs for email support
    sender_pass = 'your-gmail-password'
    receiver_address = 'address-to-send-to'
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'EMAIL_SUBJECT'
    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')

    webhook = DiscordWebhook(url='DISCORD-WEBHOOK-URL', content='WEBHOOK_MESSAGE')
    response = webhook.execute()
