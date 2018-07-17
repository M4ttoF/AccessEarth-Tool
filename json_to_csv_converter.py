#json_to_csv_converter


import json

table={}

def addTable(line):
	seperate = line.split(',')
	table[seperate[0]]=seperate[1:]


def decode(val, csv):
	#Format Lat,Long,Name,Address,PostalCode,Categories
	lat=val['location']['lat']
	lng=val['location']['lng']
	address=""
	pCode=""
	try:
		address=val['location']['address']
	except:
		pass
	try:
		pCode=val['location']['postalCode']
	except:
		pass
	s = str(lat)+','+str(lng)+','+pCode+','+address+','
	if len(val['categories']) > 0:
		categories=table[val['categories'][0]['shortName']]

		for i in categories:
			s+=i
			if not i == categories[-1]:
				s+=' '
	csv.write(s)

def main():
	getVals = open("data_backup.json", 'r',encoding="latin-1")
	values = getVals.read()
	getVals.close()

	tableFile= open("categories",'r')
	for line in tableFile:
		addTable(line)
	tableFile.close()

	dataJson = json.loads(values)
	csvFile = open("formatted.csv",'a')
	for i in dataJson:
		try:
			decode(i, csvFile)
		except:
			pass
	csvFile.close()

if __name__ == "__main__":
    main()