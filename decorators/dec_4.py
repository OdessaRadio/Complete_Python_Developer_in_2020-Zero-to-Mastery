# Practical applications

from time import time

def performance( fn ):
    def wrapper_func( *args, **kwargs):
        t1 = time()
        result  = fn(*args, **kwargs)
        t2 = time()
        print(f"Took:{ t2 - t1} ms")
        return result
    return wrapper_func


@performance
def long_time():
    for i in range(1000000):
        i*5

long_time()


user1 = {
"name": "Simon",
"is_valid": False
}

def authenticate(func):
    def wrapper(user, *args, **kwargs):
        if user["is_valid"]:
            print(f"User {user['name']} logged in.")
            return func(user, *args, **kwargs)
        else:
            print("Invalid login credentials")
    return wrapper

@authenticate
def send_message(user):
    print(f"{user['name']} sent a message")
    print("hello there mate")

send_message(user1)