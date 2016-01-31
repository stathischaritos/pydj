#!/usr/bin/python
from facepy import GraphAPI
import facepy
from pyes import *
import json
import requests
from datetime import date, timedelta
import datetime
from pickle_helpers import *
import time
from settings import *

today = datetime.date.today() 
today= today.strftime("%s")
yesterday = datetime.date.today() - datetime.timedelta(1)
yesterday= yesterday.strftime("%s")

print "Establishing ElasticSearch connection..."
conn = ES(ES_SERVER) #Connect to Elasticsearch server!
print "Initilising GraphAPI client"
graph = GraphAPI(FB_APP_EXTENDED_ACCESS_TOKEN)

print "Iterating through pages and downloading yesterdays data... "
likes_data = graph.get('me/likes')['data']
downloaded_posts = 0
for page in likes_data:
	print "Downloading data for : " , page['name']
	page_data = graph.get(str(page['id'])+'/feed' , options = {'since':str(yesterday) , 'until' : str(today)})
	while page_data:
		for post in page_data['data']:
			#Some additional metadata
			post['created_time'] = datetime.datetime.strptime(post['created_time'],'%Y-%m-%dT%H:%M:%S+0000')
			post['indexed_time'] = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

			#Take care of comment paging
			try:
				c_next = post['comments']['paging']['next']
			except:
				c_next = False
			while c_next:
				try:
					time.sleep(2)
					comments = json.loads(requests.get(c_next).text)
					post["comments"]["data"] += comments['data']
					c_next = comments['paging']['next']
				except:
					c_next = False
					
			#Take care of likes paging
			try:
				l_next = post['likes']['paging']['next']
			except:
				l_next = False
			while l_next:
				try:
					time.sleep(2)
					likes = json.loads(requests.get(l_next).text)
					post['likes']['data'] += likes['data']
					l_next = likes['paging']['next']
				except:
					l_next = False

			#Index Post in ES.
			conn.index(post, FB_INDEX_NAME , FB_INDEX_TYPE , post['id'])
			downloaded_posts += 1
			
		#Take care of posts paging
		try:
			time.sleep(2)
		 	next_page = page_data['paging']['next']
		 	page_data = json.loads(requests.get(next_page).text)
		 	#check if 'data' exists as a field.
		 	data_test = page_data['data']
		except:
			page_data = False
		
	print "Downloaded " , downloaded_posts , " posts" 



