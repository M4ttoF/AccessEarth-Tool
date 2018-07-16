#json_to_csv_converter

import json

def decode(data, csv):
	s=""
	

def main():
	fd = open("data.json", 'r')
	line = fd.readLine()
	fd.close()
	csvFile = open("formatted.csv",'w')
	arr = jsont.loads(line)
	for i in arr:
		decode(i, csv)

if __name__ == "__main__":
    main()