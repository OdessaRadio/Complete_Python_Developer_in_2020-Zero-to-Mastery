# list or set or dict comprehensions

# my_list = []
# for char in 'hello':
#     my_list.append(char)
# 
# print(my_list)

# used format
# my_list = [ param for param in iterable ]

my_list = [ char for char in 'hello' ]
# char is an expression what we are going to do with each item, we are iterating over. In this case 'hello'
#print(my_list)

my_list2 = [ num for num in range(0,100) ]
#print(my_list2)

my_list3 = [ num * 2 for num in range(0,100) ]
print(my_list3)

my_list4 = [ num ** 2 for num in range(0,100) if num % 2 == 0]
#  num ** 2 is an expression what we are going to do with each item, we are iterating over. In this case range(0,100)
# but we are going to do that only with even numbers, because of conditional statement. If true-> do
print(my_list4)