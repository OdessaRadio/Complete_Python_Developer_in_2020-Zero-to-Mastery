# Pure function - has constant transfer function
# Pure function should not have side effects on outside world

from functools import reduce

my_list = [1, 2, 3]
their_list = (10, 20, 30)

def multiply_by2(item):
    return item * 2

def only_odd(item):
    return item % 2 != 0

# map
#print( list( map( multiply_by2, my_list ) ) ) # binds function multiply_by2 and my_list taking item by item from the my_list

# filter
print( list( filter( only_odd, my_list ) ) ) # if only_odd returns true, then we add my_list item to a new list

# zip
your_list = [10, 20, 30]

print(list(zip(my_list, your_list)))
# res: [(1, 10), (2, 20), (3, 30)]

print(list(zip(my_list, your_list, their_list)))
# [(1, 10, 10), (2, 20, 20), (3, 30, 30)]

def accumulator(acc, item):
    print( acc, item )
    return acc + item

# reduce
print(reduce(accumulator, my_list, 10))