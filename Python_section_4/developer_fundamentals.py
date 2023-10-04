picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

for x in picture:
    print( f'{x}' )
print( "\n" )

fill  = '*'
empty = ' '
for row in picture:
    for pixel in row:
        if pixel :
            print( fill, end = '' ) # end = '' ends the line wothout new line
        else:
            print( empty, end = '' )
    print( '' )

'''
for row in range( 0, len( picture ) ):
    for x in range( 0, len( picture[row] ) ):
        if picture[row][x] == 0:
            picture[row][x] = ''
        else:
            picture[row][x] = '*'

for x in picture:
    print(x)
'''

# What is good code???

# 1. clean
# 2. readability
# 3. if needed make comments
# 4. predictability
# 5. DRY - Do Not Repeat Yourself

