print(list(range(100)))

def make_list(num):
    result = []
    for i in range(num):
        result.append( i* 2 )
    return result

print(make_list(100))