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
	name=val['name']
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
	s = name+','+str(lat)+','+str(lng)+','+pCode+','+address+','
	if len(val['categories']) > 0:
		categories=table[val['categories'][0]['shortName']]

		for i in categories:
			s+=i
			if not i == categories[-1]:
				s+=' '
		csv.write(s)
		return
	csv.write(s+'\n')

def main():
	getVals = open("data_backup.json", 'r',encoding="latin-1")
	values = getVals.read()
	getVals.close()

	tableFile= open("categories",'r')
	for line in tableFile:
		addTable(line)
	tableFile.close()

	dataJson = json.loads(values)
	csvFile = open("formatted.csv",'a',encoding="utf-8")
	cnt=0
	for i in dataJson:
		cnt+=1
		try:
			decode(i, csvFile)
		except:
			print(cnt)
	csvFile.close()

if __name__ == "__main__":
    main()