# *args **kwargs

def super_func( name, *args, i = "hi", **kwargs ):
    print( kwargs )
    return sum( args )

print( super_func( 'Sasha', 1, 2, 3, 4, 5, num1 = 5, num2 = 10, num3 = '' ) )

# 1, 2, 3, 4, 5 - arguments
# num1 = 5, num2 = 10, num3 = '' - keyword arguments

# Rule: params , *args, default parameteres, **kwargs
