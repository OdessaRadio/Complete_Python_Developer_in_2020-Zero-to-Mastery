from functools import reduce

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

my_numbers.sort()
print(my_numbers)

res = list( zip(my_strings, my_numbers) )

print(res)

scores = [73, 20, 65, 19, 76, 100, 88]

def check_overO50( score ):
    return score > 50

print(list(filter(check_overO50, scores)))



total = my_numbers + scores
print(f"total: {total}")


def accumulator(acc, item):
    print( acc, item )
    return acc + item

# reduce
print(reduce(accumulator, total, 0))