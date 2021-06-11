# python-surf-forecast

A Python Script to check the Surf Forecast

<img src="https://github.com/Xioto/python-surf-forecast/blob/main/docs/assets/img/logo.png" alt="logo" width="500"/>

[![GitHub Status](https://img.shields.io/github/checks-status/Xioto/python-surf-forecast/main)](https://github.com/Xioto/python-surf-forecast/)
[![Github All Releases](https://img.shields.io/github/downloads/Xioto/python-surf-forecast/total.svg?style=flat-square)](https://github.com/yuk7/wsldl/releases/latest)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
![License](https://img.shields.io/github/license/Xioto/python-surf-forecast)

## 💻Requirements
* Python 3.8
* Pip

## 📦Installation

**Note:**
1. Clone the repo
   ```sh
   git clone https://github.com/Xioto/python-surf-forecast
   ```
2. Install Python packages
   ```sh
   # Windows
   cd python-surf-forecast
   py -3 -m pip install -r requirements.txt
   
   # Unix
   cd python-surf-forecast
   python3.8 -m pip install -r requirements.txt
   ```
3. Run the `main.py` file using `python main.py` 


## 📝Configuring `main.py`

   ### Latitude & Longitude
   * Go to [Google Maps](https://www.google.com/maps) and find the Beach that you want to get a Forecast for, then Right-Click and copy the Lat & Long from Google Maps and paste it in `main.py`.

   ### API-Key
   * Go to [StormGlass](https://stormglass.io/) and click "Try for Free", you will need to Sign Up, it will then redirect you to the [Dashboard](https://dashboard.stormglass.io/). It will then provide you with an API-Key, you can then paste that in `main.py`.
   
   ### Email Support
   * To add email support, you will need to allow "[Less Secure Apps](https://myaccount.google.com/lesssecureapps) on the Google Account you are using to send the email. **WARNING** - This will make your account more vunerable to less-secure apps.
   * To remove email support, either remove the code starting from `mail_content` to `print('Mail Send')`. 
   * `mail_content` - Input the Content of the email you want to send
   * `sender_address` - Input the Email Address of the Google Account above. This will be used to send the email.
   * `sender_pass` - Input the password of the Google Account
   * `receiver_address` - Input the address that you want to send the email to.

   ### Discord Support
   * COMING SOON...

## 💸Credits

   ### API
   * [StormGlass](https://stormglass.io/)
   * [StormGlass Docs](https://docs.stormglass.io/#/)
   
   ### Tutorials
   * [Sending Emails with Python and Gmail](https://realpython.com/python-send-email/)
   * [API Get.Request Code](https://docs.stormglass.io/#/tide)
   * [Discord Webhook Support](https://pypi.org/project/discord-webhook/)
   
   ### Fixes
   * [Hiding SyntaxWarnings](https://stackoverflow.com/questions/14463277/how-to-disable-python-warnings)
   * [Finding Current Day](https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python)
   * [Finding Content in Cache_File](https://www.reddit.com/r/learnprogramming/comments/ntsu78/creating_string1_with_constantly_changing/)

## 📄License
This repository is licensed under [MIT](https://github.com/Xioto/python-surf-forecast/blob/main/LICENSE)

Copyright(c) 2021-2021 Xioto
