# find duplicates
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

print( range( 0, len(some_list) - 1 ) )

duplicates = []
for x in range( 0, len(some_list)):
    for y in range( x + 1, len(some_list)):
        if some_list[x] == some_list[y]:
            duplicates.append( some_list[x] )

print( duplicates )

dup = []
for element in some_list:
    if some_list.count( element ) > 1:
        if element not in dup:
            dup.append( element )
print( dup )