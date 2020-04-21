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

basket.insert(4,100)
print(basket)
# print(new_list)

#remkoving
basket.pop() # removing the last element
basket.pop(0) # removes item in the selected index. 0 here
basket.remove(4) # removed selected value

new_list = basket.remove(100)

print(basket)
print(new_list)

new_list = basket.pop(4) # pop returns 4 element into new_list

print(basket)
print(new_list)

new_list = basket.clear() # just clear the list. Returns nothing

print(basket)
print(new_list)

#2_43
# List Methods 2

