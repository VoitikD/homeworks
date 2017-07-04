#1
list1 = [1, 211, 6, 34, 68, 9]
list1.sort()
print(l)

#2
dict1 = {4: '4', 
12: '12', 
99: '99', 
11: '11', 
5: '5'}

for k, v in dict1.items():
	print(k, v)

#3
tuple1 = (0.5, 0.9, 2.8, 10.2, 1.5, 0.1, 2.3, 11.1, 1.2, 1.0)

print(max(tuple1), min(tuple1))		

#4
list2 = ['Earth', 'Russia', 'Moscow']
list_sum = list2[0] + list2[1] + list2[2]
print(list_sum)

#5
string = '/bin:/usr/bin:/usr/local/bin'.split(':')
print(string)

#6
list_result = []
for i in range(1, 101):
	if i % 7 == 0:
		list_result.append(i)
	else: continue	
print(list_result)	

#7
matrix = [
    [0, 1, 2],
    [4, 5, 6],
    [8, 9, 10],
    [12, 13, 14]
] 

for row in matrix:
	print(row)
	
#не могу придумать ничего со столбцами

#8 

list_of_objects = [1, 'dog', 22, 'cat']
for i in list_of_objects:
	print(i, list_of_objects.index(i))

#9

list_to_del = [1, 'to-delete', 'dog', 'to-delete', 22, 'to-delete', 'cat']
while 'to-delete' in list_to_del:
	list_to_del.remove('to-delete')
print(list_to_del)

#10

for i in range(10, 0, -1):
	print(i)








	
