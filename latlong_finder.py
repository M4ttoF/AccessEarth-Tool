#latlong_finder

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
import sys


def restartDriver(num, driver):
	print("Trying to close!")
	driver.close()
	print("Closed!")
	time.sleep(1)
	driver2=webdriver.Chrome()
	driver2.get("https://www.latlong.net/")
	return driver2



def stripName(name):
	name=name[:-1]
	name=name.split()
	newName=""
	for i in name:
		newName+=i+' '
	newName	=newName[:-1]
	return newName


def getCoords(name, lastLat, num, driver, coords):
	newName=stripName(name)
	try:
		inputBox = driver.find_element_by_class_name("width70")
		button = driver.find_element_by_class_name("button")
		inputBox.clear()
		inputBox.send_keys(newName)
		while(True):
			time.sleep(1)
			button.click()
			time.sleep(1)
			latBox = driver.find_element_by_id("lat")
			longBox = driver.find_element_by_id("lng")
			newLat = latBox.get_attribute('value')
			newLong = longBox.get_attribute('value')
			if newLat!=lastLat and newLat!="":
				break
		print("Adding", newName, 'at', newLat, newLong)
		coords.write(newLat+' '+newLong+'\n')
		return newLat
	except:
		driver = restartDriver(num, driver)
		return getCoords(name, lastLat, num, driver, coords)



def main(startAt):
	driver=webdriver.Chrome()
	action=ActionChains(driver)

	driver.get("https://www.latlong.net/")

	cities = open("CanadaCities.txt", 'r')
	coords = open("CandaCityCoords.txt", 'a')


	lastLat = 900
	i=0
	for line in cities:
		i+=1
		if i >= int(startAt):
			lastLat = getCoords(line, lastLat, i, driver, coords)

	cities.close()
	coords.close()


if __name__ == "__main__":
    main(sys.argv[1])