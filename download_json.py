#Access Earth Scraper
#Matthew Farias
'''

payload={'key1': 'value1', 'key2': 'value2'}
#r = requests.post("https://httpbin.org/post")
r = requests.post("https://httpbin.org/post", data = payload)
print(r.text)
'''

import time
import requests	
import urllib

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities    

# enable browser logging
d = DesiredCapabilities.CHROME
d['loggingPrefs'] = { 'browser':'ALL' }
driver = webdriver.Chrome(desired_capabilities=d)
action=ActionChains(driver)


CITY = "Windsor"


#Logs into the app
def login(driver,action):

	driver.get("https://access.earth/app/")

	elem = driver.find_element_by_name("username")

	action.move_to_element(elem)
	action.move_by_offset(xoffset=110,yoffset=325)
	action.click()
	action.send_keys("spellyy")
	action.move_by_offset(xoffset=500,yoffset=0)
	action.click()
	action.send_keys("qpwoeiruty")
	action.move_by_offset(xoffset=0,yoffset=50)
	action.click()
	action.perform()
	action.reset_actions()
	time.sleep(3)	

	searchFor(driver, action)	


#Searches for the city on the app
def searchFor(driver, action):

	elem=driver.find_element_by_name("search")
	action.move_to_element(elem)
	action.click()
	action.perform()
	action.reset_actions()
	time.sleep(2)

	elem = driver.find_element_by_class_name("searchbar-input")

	elem.send_keys(CITY)
	elem=None
	time.sleep(1)
	while elem == None:
		arr = driver.find_elements_by_class_name("label-md")
		try:
			elem = arr[4]
		except:
			time.sleep(1)
	elem.click()
	time.sleep(2)
	getNetworkRequests(driver,action)

#Searches through the network requests and finds the one with the JSON data with locations
def getNetworkRequests(driver, action):
	script = "var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;"
	data = driver.execute_script(script)
	for i in data:
		if 'factual_data' in i['name']:
			url = i['name']
			break
	downloadJsonLink(url)

#Goes to URL link and downloads the JSON data to a file named after the city
def downloadJsonLink(url):
	data=urllib.request.urlopen(url)
	data=data.read()
	print(data)
	file = open(CITY + '.JSON', 'w')
	file.write(str(data))
	file.close()

login(driver, action)

driver.close()