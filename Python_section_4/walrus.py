a = 'helloooooooo'
if( ( n:= len( a ) ) > 10 ): # := - walrus operator
    print( f"too long {n} elements" )

while( ( n := len( a ) ) > 1 ):
    print(n)
    a = a[:-1]


c = [1, 3, 5, 6, 8,10, 13, 15, 20]
print( c[6:2:-1] )
print( c[:-3] )