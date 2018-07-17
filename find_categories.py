#find_categories

import json

found = {}

def findCats(val, out):
	catArr=val['categories']
	if len(catArr)==0:
		return
	cat = catArr[0]['shortName']
	if cat not in found:
		found[cat] = True
		out.write(cat+'\n')


def main():
	fd = open("data_backup.json", 'r',encoding="latin-1")
	line = fd.read()
	fd.close()
	cats = open("categories",'a')
	arr = json.loads(line)
	for i in arr:
		findCats(i, cats)
	cats.close()

if __name__ == "__main__":
    main()