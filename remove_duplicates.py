#remove_duplicates

from ast import literal_eval

print("Did you fix the file to make it one line of a json list?\n(y/n)")
ans = input()
if ans=='n':
	exit()

fd= open('data.json', 'r')
read_data= fd.read()
fd.close()

values = literal_eval(read_data)
values=set(values)

fd = open('fixed_data.json','w')
fd.write(values)
fd.close()