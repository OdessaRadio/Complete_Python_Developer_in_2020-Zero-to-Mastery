# Tuple 2_53

# Tuples are immutable

my_tuple = (1,2,3,4,5)
# print(my_tuple[1])

# print(5 in my_tuple) # check 5 absence in my_tuple

user = {
  'basket': [1,2,3],
  'greet' : 'hello',
  'age' : 20,
  (1,2,3,4) : ('a', 'b', 'c')
}

# print(user.items())

# print(user[(1,2,3,4)])

# Tuples 2  2_54

my_tuple = (1,2,3,4,5,1,1,1,1)

new_tuple = my_tuple[1:2]

x = my_tuple[0]
y = my_tuple[1]

# print(x,y)

# print(new_tuple)

x,y,z, *other = (1,2,3,4,5,1,1,1)
# print(other)

print(my_tuple.count(5))

print(my_tuple.index(1)) 

print(len(my_tuple))


