# Error handling
# errors and exceptions

while True:
    try:
        age = int(input( 'what is your age? ' ))
        10 / age
        #print(age)
        raise Exception('hey cut it out')
    except ZeroDivisionError:
        print("please, enter age higher than 0")
        break

    except Exception:
        print('dsadsadsadsadsad')


    else:
        print("thank you")
    finally: # runs after everything was executed
        print('ok i am finally done')

    print('can you hear me?')