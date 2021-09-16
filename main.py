# main.py for python-surf-forecast
# Author: Xioto
# Licensed under the MIT License

import requests  # for API requests
import datetime  # for finding date
import warnings  # for ignoring SyntaxWarnings
import json  # for caching API response
import smtplib  # for sending emails
import sys  # for printing dots
import discord_webhook  # for discord webhook
from discord_webhook import DiscordWebhook  # renaming
from email.mime.multipart import MIMEMultipart  # for adding HTML email support (coming soon...)
from email.mime.text import MIMEText  # for sending Basic Text in emails
from time import sleep  # see sys comment

CURRENT_VERSION = 1.6


def send_email(mail_content, from_address, from_pass, to_address):
    """
    Sends an email with the provided content.

    :param mail_content: The content of the email
    :param from_address: The address we're sending the email from
    :param from_pass: The password to log in
    :param to_address: Who we're sending the email to.
    :return:
    """

    message = MIMEMultipart(From=from_address, To=to_address, Subject='EMAIL_SUBJECT')
    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(from_address, from_pass)
    text = message.as_string()
    session.sendmail(from_address, to_address, text)
    session.quit()
    print('Mail Sent')


def main(lat, long, send_as_email=False):
    """
    Checks the wave conditions at a given surf location.

    :param send_as_email: Whether to send the result as an email.
    :param lat: The latitude of the surf location to check.
    :param long: The longitude of the surf location to check.
    :return:
    """

    print('''
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

    check_current_version(CURRENT_VERSION)

    cache_file = 'response.json'
    data = []

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        warnings.warn("deprecated", DeprecationWarning)

    weekno = datetime.datetime.today().weekday()  # finds current date
    if weekno > 4:  # if today is a weekend
        print(f"Attempting to load {cache_file}")
        with open(cache_file, 'r') as f:  # opens cache_file
            data = json.load(f)

    response = requests.get(  # sends request to API
        'https://api.stormglass.io/v2/weather/point',
        params={
            'lat': lat,
            'lng': long,
            'params': 'waveHeight',
        },
        headers={
            'Authorization': 'auth-key'  # read docs on how to get an API key
        }
    )

    data = response.json()
    print(f"Writing json cache to {cache_file}")
    with open(cache_file, 'w') as f:
        json.dump(data, f)  # dumps response from API in response.json (cache_file)

    content = ''
    for hourly_data in data.get('hours', None):
        if 'waveHeight' in hourly_data.keys() and hourly_data['waveHeight']['dwd'] >= 0.6:
            print('Found')
            content = hourly_data

        # to enable email support, see the docs or README.md
        if send_as_email:
            send_email(content, from_address=None, from_pass=None, to_address=None)

        # to enable discord support, see the docs or README.md
        ##webhook = DiscordWebhook(url='DISCORD-WEBHOOK-URL', content='WEBHOOK_MESSAGE')
        ##response = webhook.execute()
        break
    else:
        print("No Surf Found!")


def check_current_version(cur_version):
    """
    Check that we're using the latest version of the script.
    Exits the program with an error if not using the latest version.

    :param cur_version:
    :return:
    """

    print("Checking for updates")

    words = "................."

    for char in words:
        sleep(0.3)
        sys.stdout.write(char)
        sys.stdout.flush()

    if cur_version == 1.6:
        print('''
    You are up to date!''')

    else:
        print("You are Out-of-Date! Please update at https://github.com/Xioto/python-surf-forecast/releases/")
        sys.exit(1)


if __name__ == '__main__':
    # add your surf location latitude and longitude here
    surf_latitude = 0
    surf_longitude = 0

    # These values are needed if an email is going to be sent...
    from_address = 'your-gmail-address'
    from_pass = 'your-gmail-password'
    to_address = 'address-to-send-to'


    main(surf_latitude, surf_longitude)
