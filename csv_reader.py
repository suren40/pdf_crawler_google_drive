import csv 
with open('link.csv','rt') as f:
	reader = csv.reader(f)
 	item_list = list(reader)
	sorted_list = item_list.sort()
print(len(item_list))
for i in range(10,len(item_list)):
	print(item_list[i][0])
	print(item_list[i][1])
print(list(set(sorted_list)))
