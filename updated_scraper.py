#updated_json_scraper

import urllib
import requests
import time
import io

found={}

def scrapeLocation(city):
	city = city.split()
	centerLat = float(city[0])
	centerLong = float(city[1]) 
	long1 = centerLong - 0.00547608948
	long2 = centerLong + 0.00547608948
	lat1 = centerLat - 0.0026599506
	lat2 = centerLat + 0.0026599506

	url="https://access.earth/php/factual_data.php?lat="+str(centerLat)+"&lng="+str(centerLong)+"&bounds="+str(long1)+","+str(lat1)+","+str(long2)+","+str(lat2)+"&q=e&user=1"
	print(url)
	data=requests.get(url)
	if len(data.text) < 10:
		return ""
	#print(data.json()[0])
	return checkDup(data.json())

def checkDup(arr):
	out=[]
	for i in arr:
		if i['id'] not in found:
			out.append(i)
			found[i['id']]=True
	return str(out)

def main():	
	latX=-90
	longX=-126.021358
	fd=open('CanadaCityCoords.txt', 'r')
	saveData=io.open('data.json', 'a', encoding="utf-8")
	i=0
	for line in fd:
		i+=1
		if i > 3162:
			saveData.write(scrapeLocation(line))
			print("Writing from location", line)
	#scrapeLocation("43.653226 -79.383184")
	#scrapeLocation("42.314937 -83.036363")
	saveData.close()
	fd.close()
if __name__ == "__main__":
    main()

'''
	
'''