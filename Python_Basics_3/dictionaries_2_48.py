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
print(dict_13['123'])
# Dict key should be unique!

