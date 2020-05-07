# Set   2_55

# set -> unordered collection of unique objects

my_list = [1,2,3,4,5,5,6,6,7,7,8]

my_set = {1,2,3,4,5,5,6,6,7,7,81,2,3,4,5,5} # set
my_set.add(2)
my_set.add(100)

print(1 in my_set)
print(len(my_set))

print(list(my_set))

print(set(my_list)) # Remove all duplicates from the list

new_set = my_set.copy()

my_set.clear()
print(my_set)

