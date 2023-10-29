# lambda expressions - one time anonymous function that we dont need more than once
# function is used once, no storing it in memory

# lambda param: action(param)

def mult( arg ):
    return arg * arg

my_list = [5, 3, 2]

print(list(map( lambda i: i ** 2, my_list )))



a = [(0, 2), (4, 3), (9, 9), (10, -1)]

#a.sort(key = 1)
#a.sort(key = lambda x: x[1])
print( (lambda x: x[1])(a))


A = [1, -2, -5, -6, 10, 102]
print( (lambda i : i[2]) (A) )