from pickle_helpers import *
#Global Settings File

#Facebook Authorisation Info
FB_APP_ID = "*********"
FB_APP_SECRET_KEY = "******************"
#You can get the short access token from developers.facebook.com under tools -> Access Tokens -> User Token . This needs to be updated before running the update_fb_access_token script.
FB_APP_SHORT_USER_ACCESS_TOKEN  = '*****************'
FB_APP_EXTENDED_ACCESS_TOKEN = load_pickle("fb_extended_access_token.pkl")

#ElasticSearch Server Info
ES_SERVER = 'localhost:9200'
FB_INDEX_NAME = "facebook"
FB_INDEX_TYPE = "post"
TWITTER_INDEX_NAME = "twitter"

