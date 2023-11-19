def generator_function( num ):
    for i in range(num):
        yield i # instead if creating the list in memory we return value by vaue with yield

# because we have yield the function returns one vlue at a time
# if we use next with reference to a function, the function with yield will return next value
# yeild pauses the function and comes back to it on next call
# the function with yield remembers how many times we call it before

g = generator_function(100)
print(g)
next(g)
print(next(g))
print(next(g))
print(next(g))

#def make_list(num):
#    result = []
#    for i in range(num):
#        result.append( i* 2 )
#    return result


