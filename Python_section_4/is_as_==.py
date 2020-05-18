# is as == 4_65

print(True is True)
print('1' is '1')
print([] is []) # False because adding a list is a new location in the memory
print(10 is 10.0)
print([1,2,3] is [1,2,3]) # data structure. Each time we create it, it is located in new memory area

a = [1,2,3]
b = [1,2,3]

print(a == b)

# == checks for equality of Values. Different data types will be converted to bool

# is check is the location in the memory were the value is stored is the same


