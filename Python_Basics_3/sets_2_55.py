# Set   2_55

# set -> unordered collection of unique objects

my_list = [1,2,3,4,5,5,6,6,7,7,8]

my_set = {1,2,3,4,5} # set
your_set = {4,5,6,7,8,9,10}
my_set.add(2)
my_set.add(100)

# print(1 in my_set)
# print(len(my_set))
# print(list(my_set))
# print(set(my_list)) # Remove all duplicates from the list

new_set = my_set.copy()

my_set.clear()
# print(my_set)

my_set = {4,5} # set
your_set = {4,5,6,7,8,9,10}

# difference method
# print(my_set.difference(your_set))
# print(my_set)
# print(your_set.difference(my_set))

# discard method
# print(my_set.discard(5))
# print(my_set)

# difference_update
# print(my_set.difference_update(your_set))
# print(my_set)

# intersection
#print(my_set.intersection(your_set))
#print(my_set & your_set)


# isdisjoint
# print(my_set.isdisjoint(your_set))

# union
#print(my_set.union(your_set))
#print(my_set | your_set)

# issubset
# print(my_set.issubset(your_set))

# issuperset
# print(my_set.issuperset(your_set))

