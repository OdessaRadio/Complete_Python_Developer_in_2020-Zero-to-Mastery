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

print(user.items())

print(user[(1,2,3,4)])

