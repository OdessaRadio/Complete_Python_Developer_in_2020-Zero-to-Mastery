try:
    with open('./Complete_Python_Developer_in_2020-Zero-to-Mastery/IO/test.txt', mode = 'r') as my_file:
        text = my_file.readlines()
except FileNotFoundError as err:
    print('File does not exist')
    raise err
except IOError as err:
    print('IO Error')
    raise err
print(text)