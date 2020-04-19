# formatted strings

name = "Johnny"
age = 55

# print('Hi '+ name + '. You are ' + str(age))

print(f'Hi, {name}. You are {age} yers old') # f tells Python that this is formatted string

print('Hi, {}. You are {} yers old'.format('Johnny', '55'))
print('Hi, {}. You are {} yers old'.format(name, age))

print('Hi, {1}. You are {0} yers old'.format(name, age))
print('Hi, {1}. You are {0} yers old'.format(name, age))

print('Hi, {new_name}. You are {new_age} yers old'.format(new_name='Sasha', new_age=32))
