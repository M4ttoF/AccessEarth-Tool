# Access Earth Scraper
# Matthew Farias
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

found ={}


# Logs into the app
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


#Searches for the city on the app
def searchFor(driver, action, location):

	elem=driver.find_element_by_name("search")
	action.move_to_element(elem)
	action.click()
	action.perform()
	action.reset_actions()
	time.sleep(3)

	elem = driver.find_element_by_class_name("searchbar-input")

	name=""
	name=str(name)
	for i in range(len(location)):
		name+= location[i]
		if i!= location[-1]:
			name+= ' '

	print(name)
	elem.send_keys(name)
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
	getNetworkRequests(driver,action, location)

#Searches through the network requests and finds the JSON data with locations
def getNetworkRequests(driver, action, location):
	script = "var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;"
	data = driver.execute_script(script)
	for i in data:
		if 'factual_data' in i['name'] and i['name'] not in found:
			downloadJsonLink(i['name'], location)
			found[i['name']] = True

#Goes to URL link and downloads the JSON data to a file named after the city
def downloadJsonLink(url, location):
	data=urllib.request.urlopen(url)
	data=data.read()
	print("Adding in data for",location)
	city=""
	for i in range(len(location)-1):
		city+= location[i]
		if i!= location[-2]:
			city+= ' '
	city=city[:-1]
	file = open("Canada\\"+location[-1]+"\\"+city+'.JSON', 'w')
	file.write(str(data))
	file.close()

login(driver, action)

searchFile = open("CanadaCities.txt", 'r')
for line in searchFile:
	print(line.split())
	searchFor(driver, action, line.split())


driver.close()