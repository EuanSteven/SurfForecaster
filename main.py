# main.py for python-surf-forecast
# Author: Xioto
# Last updated: 10/06/2021
# Version 1.1
# Latest Change: Added Email Support
# Next Change: Add HTML Email Support, add Error Handling and change from "ignore all" to ignoring only SyntaxWarnings
# Licensed under the MIT License

import requests # for API requests
import datetime # for finding date
import warnings # for ignoring SyntaxWarnings
import json # for caching API response
import smtplib # for sending emails
from email.mime.multipart import MIMEMultipart # for adding HTML email support (coming soon...)
from email.mime.text import MIMEText # for sending Basic Text in emails

cache_file = 'response.json'
data = []

print("""\
ＴＨＡＮＫ ＹＯＵ ＦＯＲ  ＵＳＩＮＧ ＴＨＥ ＰＹＴＨＯＮ－ＳＵＲＦ－ＦＯＲＥＣＡＳＴ
               """)
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
    "Hi!\nTHe Python script has detected surf at your-location\nHere is the link to MagicSeaweed:\nhttps://magicseaweed.com
    \n I am a Bot, if I am wrong, and there is no surf, please contact Xioto."
    ''' # content for email
    sender_address = 'your-gmail-address' # see docs for email support
    sender_pass = 'your-gmail-password'
    receiver_address = 'address-to-send-to'
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Check MagicSeaweed for Surf Forecast'
    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')
