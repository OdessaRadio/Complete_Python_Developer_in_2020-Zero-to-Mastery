# formatted strings

# name = "Johnny"
# age = 55

# # print('Hi '+ name + '. You are ' + str(age))

# print(f'Hi, {name}. You are {age} yers old') # f tells Python that this is formatted string

# print('Hi, {}. You are {} yers old'.format('Johnny', '55'))
# print('Hi, {}. You are {} yers old'.format(name, age))

# print('Hi, {1}. You are {0} yers old'.format(name, age))
# print('Hi, {1}. You are {0} yers old'.format(name, age))

# print('Hi, {new_name}. You are {new_age} yers old'.format(new_name='Sasha', new_age=32))


# string indexes

selfish = '01234567'
          #01234567
print(selfish[0])
print(selfish[7])
print(selfish)

# [start:stop:stepover]
print(selfish[0:8:3])

print(selfish[1:])
print(selfish[:5])
print(selfish[::2])
print('#')
print(selfish[-2]) # Negative index means to start from the end of the string
print(selfish[::-1])
print(selfish[::-2])

