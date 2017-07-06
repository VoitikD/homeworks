#Errors
#1
number = int(input('Please input a number '))
try:
    if number % 2 == 0:
        raise ValueError('Number is even')
    elif number < 0:
        raise TypeError('Number is negative')     
    elif number > 10:
	    raise IndexError('Number is greater than 10')
except Exception as ex:
	print(ex)

#2

l = [1, 'asd', 43, 100, 'kkk', True]
try:
	index = int(input('Please input an index '))
	print('Here is the element you are lookinf for: ', l[index])
except ValueError as ex:
    print('That was not a number \n{}'.format(ex))
except IndexError as ex:
	print('There are no such index \n{}'.format(ex))

#Functions1
#1
def sum_not_sum(x, y):
    if x > 0 and y > 0:
        return x + y
    if x < 0 and y < 0:
        return (x) - (y)
    if x > 0 and y < 0 or x < 0 and y > 0:
        return 0
print(sum_not_sum(-2, -12))

#2
def three_numbers(a, b, c):
	l = [a, b, c]
	l.sort(reverse=True)
	return l[0:2]

print(three_numbers(1, 43, 12))

#3 смог сделать только в лоб, 
#но наверняка можно сделать все гораздо изящнее и раза в 2 короче
def bool_list(my_list, odd):
    if odd:
    	odd_list = []
    	for i in my_list:
    		if i % 2 != 0: odd_list.append(i)  
    	return odd_list	
    even_list = []
    for i in my_list:
    	if i % 2 == 0: even_list.append(i) 
    return even_list
    	 
print(bool_list([1, 2, 3, 4, 5, 6, 7], True))
print(bool_list([1, 2, 3, 4, 5, 6, 7], False))


#Functions2
#1
def min_max_func(*args):
	return min(args), max(args)
print(min_max_func(1, 1212, 99999, 42))	

#2
def my_string(my_string, case=True):
    if case:
    	return my_string.upper()
    else:
    	return my_string.lower()

print(my_string('python is a beatiful language'))
print(my_string('AAAABBBBBCCCC', False))    	


#3
def glue_func(*args, glue=':'):
    for i in (args):
    	l = []
        if len(i) > 3: l.append(i + glue)
    return l   

print(glue_func('12', 'asdff', '4312', '12', 'qwerty'))


