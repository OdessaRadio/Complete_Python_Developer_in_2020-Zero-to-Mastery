picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
for x in picture:
    print(f'{x}')
print("\n")

for row in picture:
    for pixel in row:
        if( pixel == 1):
            print('*', end = '') # end = '' ends the line wothout new line
        else:
            print(' ', end = '')
    print('')

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