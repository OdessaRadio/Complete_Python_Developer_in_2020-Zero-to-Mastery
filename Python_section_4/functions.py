# functions
def say_hello( arg1 = "dsad", arg2 = "dsads" ):
    print( f'{arg1}{arg2}' )

say_hello()
print(say_hello)

say_hello( "123213" )

def sum( func ):
    def func():
        print("func")

sum( 1 )

