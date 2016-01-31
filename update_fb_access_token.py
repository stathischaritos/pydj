#!/usr/bin/python
from facepy import GraphAPI
import facepy
from pyes import *
import json
import requests
from datetime import date, timedelta
import datetime
from pickle_helpers import *
from settings import *

today = datetime.date.today() 
today= today.strftime("%s")
yesterday = datetime.date.today() - datetime.timedelta(1)
yesterday= yesterday.strftime("%s")

#Get new extended access token!
extended_access_token, expires_at = facepy.utils.get_extended_access_token(FB_APP_SHORT_USER_ACCESS_TOKEN, FB_APP_ID, FB_APP_SECRET_KEY)
print "Received extended access until : " , expires_at
print extended_access_token

save_pickle(extended_access_token,"fb_extended_access_token.pkl")
