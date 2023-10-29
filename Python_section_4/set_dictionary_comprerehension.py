simple_dictionary = {'a':1, 'b':2}
my_dict = {key * 2 : value ** 2 for key,value in simple_dictionary.items() if value % 2 == 0 }
print(my_dict)

# key * 2 : value ** 2 -> this section shows us what we want to do with data
# for key,value in simple_dictionary.items() -> for loop

ny_dict = { num:num * 2 for num in [1,2,3]}
print(ny_dict)


some_list = ['a', 'b', 'c', 'b','d', 'm', 'n', 'n']

duplicates = list(set([i for i in some_list if some_list.count(i) > 1]))
print(duplicates)

