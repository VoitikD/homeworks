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