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
print(amazon_cart)
print(new_cart)

amazon_cart[2] = 'cherry'
print(amazon_cart)
print(new_cart)


new_cart = amazon_cart[:] # [:] -> slicing the list, create a copy
new_cart[0] = 'ball'
print(amazon_cart)
print(new_cart)

amazon_cart[2] = 'rocket'
print(amazon_cart)
print(new_cart)

# every time we do slicing we create a new object
