# first class citizens
def hello(func):
    print("Hellooooo")
    func()

def func1():
    print("still here")

a = hello(func1)

a

#greet = hello
#del hello
#greet()
#print(hello)
#print(greet)
#
#print(greet())