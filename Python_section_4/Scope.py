# function scope

# sequence of scope check by python interpreter
# 1 start with local
# 2 parent local
# 3 global
# 4 built in Python functions




#a = 10
#def confusion( b ):
#    print( b )
#    a = 90
#
#confusion( 300 )

#total = 0
#def count():
#    global total  # means to use global variable total if it exists
#    total += 1
#    return total
#
#count()
#print( count() )


# Dependency injection
total = 0
def count( total ): # taotal as argument is a dependency injection
    total += 1
    return total

count( total )
print( count( total ) ) 