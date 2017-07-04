







#Functions
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
        if len(i) > 3:
    	    print(i, glue)
        else: continue    

glue_func('12', 'asdff', '4312', '12', 'qwerty')

# реализовать печать в одну строку, а не построчно!

