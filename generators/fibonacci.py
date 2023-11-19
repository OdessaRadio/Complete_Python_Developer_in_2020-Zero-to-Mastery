class Num:
    a = 0
    b = 1
    res = 0

def fib(index):
    for i in range(index-1):
        Num.res = Num.a + Num.b
        Num.a = Num.b
        Num.b = Num.res
    return Num.res

print(fib(11))
