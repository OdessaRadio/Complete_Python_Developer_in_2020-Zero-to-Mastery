# Dictionary
# 2_48

dictionary = {
  'a' : [1,2,3],
  'b' : 'hello',
  'x' : True
}

my_list=[
  {
  'a' : [1,2,3],
  'b' : 'hello',
  'x' : True
},
{
  'a' : [4,5,6],
  'b' : 'hello',
  'x' : True
}
]

# print(my_list[0]['a'][2])
# print(dictionary['b'])

# Understanding Data Structures
# 2_49 

# Dictionary has no orde
# List is ordered

# Dictionary holds more information than a list
# Liat is just an index and Value

dict_10 ={
  'weapons' : [1,2,3],
  'greeting' : 'hello',
  'is_Magic' : True
}

# Dictionary Keys
# 2_50

dict_11 ={
  123 : [1,2,3],
  'greeting' : 'hello',
  'is_Magic' : True
}

# print(dict_11[123])

dict_12 ={
  123 : [1,2,3],
  True : 'hello',
  'is_Magic' : True
}

# print(dict_12[True])

dict_13 ={
  '123' : [1,2,3],
  '123' : 'hello'
}

#print(dict_12[100]) # Keys should be immutable. 
# print(dict_13['123'])
# Dict key should be unique!

# Sictionary Methods
# 2_51

dict_14 ={
  'basket' : [1,2,3],
  'greet' : 'hello'
}

# print(dict_14['basket'])

user ={
  'basket' : [1,2,3],
  'greet' : 'hello',
  'age' : 20
}

# print(user.get('age')) # Return None if no 'age'
# print(user.get('age', 55)) # If no 'age' key return 55

user2 = dict(name = 'JohnJohn') # Another way to create a dict

# print(user2)


# Dictionary Methods 2
# 2_52

# print('age' in user.keys())
# print('hello' in user.values())

# print('age' in user.items()) # Grabs the entire item -> returns list of tuples
user2 = user.copy()
user.clear() # clear does not return anything

# print(user)
# print(user2)

# user2.pop('age') # returns the selected value and removes it from dict
# print(user2)

# user2.popitem() # removes last item in dict
# print(user2)

print(user2.update({'age' : 55}))
print (user2)

