# 2_38

user_name = input('Enter your name: \n')
user_secret = input('Enter your password: \n')

# user_secret_len = len(user_secret)
user_secret_converted = str(len(user_secret) * '*')

# print(user_secret_len)
print(f'{user_name}, your password {user_secret_converted} is {len (user_secret)} letters long')
