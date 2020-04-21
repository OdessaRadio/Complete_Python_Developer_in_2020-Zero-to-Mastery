# 2_39
# lists

li = [1,2,3,4,5]
li2 = ['a', 'b', 'c']
li3 = [1,2.5,'d','e',True]

# Data Structure

amazon_cart = [
  'notebooks',
  'sunglasses',
  'toys',
  'grapes'
]
# print(amazon_cart[0])
# print(amazon_cart[1])

# 2_40
# List slicing

string = '01234567889'
# print(string[0:6:1])

# print(amazon_cart[0:3])

amazon_cart[0] = 'laptop' # lists are mutable
new_cart = amazon_cart # pointer to the same memory area
new_cart[0] = 'gum'
# print(amazon_cart)
# print(new_cart)

amazon_cart[2] = 'cherry'
# print(amazon_cart)
# print(new_cart)


new_cart = amazon_cart[:] # [:] -> slicing the list, create a copy
#new_cart = amazon_cart.copy() -> returns new list
new_cart[0] = 'ball'
# print(amazon_cart)
# print(new_cart)

amazon_cart[2] = 'rocket'
# print(amazon_cart)
# print(new_cart)

# every time we do slicing we create a new object

# 2_41
# Matrix

matrix = [
  [1,5,1],
  [0,1,0],
  [1,0,1]
  ] # X letter representation


# print(matrix[0][1])

# 2_42 
# List Methods

basket = [1,2,3,4,5]
# adding
new_list = basket.append(1000)

basket.extend([100,101])

basket.insert(4,100) # set position and value to insert to the list
# print(basket)
# print(new_list)

#remkoving
basket.pop() # removing the last element
basket.pop(0) # removes item in the selected index. 0 here
basket.remove(4) # removed selected value

new_list = basket.remove(100)

# print(basket)
# print(new_list)

new_list = basket.pop(4) # pop returns 4 element into new_list

# print(basket)
# print(new_list)

new_list = basket.clear() # just clear the list. Returns nothing

# print(basket)
# print(new_list)

#2_43
# List Methods 2

basket = ['a','b','c','d','e', 'd']
# print(basket)

# print(basket.index('c')) # returns index of the value

# print(basket.index('b',1,4)) # searching 'from' to 'to' for the value and returns index

# python key word "in"
# print('d' in basket) # checking 'd' value in basket. returns True
# print('x' in basket) # checking 'x' value in basket. returns False

# print('i' in ',mds;lmdaslinflnfgl')

# print(basket.count('d')) # returns how many time value occures

# 2_44
# List Methods 3

cart = ['a','x','b','c','d','e','d']

# print(cart.sort()) # .sort() method modifies the list. Returns nothing

# print(cart)

# sorted(cart)

# print(sorted(cart)) # "sorted" doesn't modify cart, it creates new object
# print(cart)

#print(cart.reverse()) # .reverse() doesn't return anything. ,.reverse() modifies the list

# cart.reverse()
# print(cart)

# 2_45
# Common List Patterns

print(cart[::-1]) # creates a new object
print(cart)

print(list(range(100))) # start, stop

sentence = ' '
new_sen = sentence.join(['Hi' , 'my', 'name', 'is', 'JOJO']) # sentence takes a role of the jointer
new_sen2 = '\''.join(['1','2','3','4','5']) # one of the ways to combine list into string
print(sentence)
print(new_sen)
print(new_sen2)

list_1 = ['a', 'b', 'c', 'e', 'z']
list_2 = ['d', 'x']
print( sorted(list_1+list_2))
