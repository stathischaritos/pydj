# This script gets historical facebook data using the netvizz app.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import selenium.webdriver.support.ui as ui
import re
from helpers import *


def handle_page(Name , Code , driver , s_date , e_date):
	print "Handling page :" + Name + "..."
	link = 'https://tools.digitalmethods.net/netvizz/facebook/netvizz/index.php?module=pages&action=pages&pageid='+ Code +'&posts=50&fromwho=feed&override=true&since='+ s_date + '&until='+ e_date
	driver.get(link)
	driver.find_element_by_link_text('tsv comments file').click()
	data =  BeautifulSoup( driver.page_source ).text
	f = open("".join(name.split(" ")) + '_' + "".join(start_date.split("-")) + '_' + "".join(end_date.split("-")) +'.tab', 'w')
	f.write(data.encode('utf8'))
	f.close()
	print "Done!"


start_date = "2010-01-01"
end_date = "2010-01-02"
username = '******************'
password = '*****************'

netvizz_page_data = "https://tools.digitalmethods.net/netvizz/facebook/netvizz/index.php?module=pages"



browser = webdriver.Firefox()
wait = ui.WebDriverWait(browser,10)

print "Connecting to Facebook.com..."
browser.get('http://www.facebook.com')

print "Logging in to profile : " + username + " ..."
browser.find_element_by_id('email').send_keys(username)
browser.find_element_by_id('pass').send_keys(password)
browser.find_element_by_id('u_0_n').click()

browser.get(netvizz_page_data)
availlable_pages = wait.until(lambda availlable_pages: browser.find_elements_by_link_text('post by page only'))

pages = []

for page in availlable_pages:
	code = re.findall(r'\d+',page.get_attribute("href"))[0]
	name = page.find_element_by_xpath('..').text.split("( post by page only")[0].strip()
	pages += [[name , code]]
	handle_page(name,code,browser,start_date,end_date)




