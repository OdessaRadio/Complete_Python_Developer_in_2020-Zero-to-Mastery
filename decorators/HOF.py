# Higer order function - HOF
# is a function that receives or returns another function

def greet(func):
    func()

def greet2():
    def func():
        return 5
    return func
