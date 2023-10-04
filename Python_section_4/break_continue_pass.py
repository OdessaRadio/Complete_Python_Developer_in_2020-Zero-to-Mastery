my_list = [1,2,3]

for item in my_list:
    print( item )
    continue

i = 0
while i < len( my_list):
    print(my_list[i])
    i += 1
    continue

for item in my_list:
    pass # use if we dont know what we are going to do here
    ...
    print( item )