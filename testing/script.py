import random

print(__name__)

def run_guess(guess, answer):
    try:
        if 0 < guess < 11:
            if guess == answer:
                print('you won')
                return True
        else:
            print('please, select from 1 to 10')
            return False
    except TypeError as err:
        print('please enter a number')
        return err


if __name__ == '__main__':
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input('guess a number 1 to 10: '))
            if(run_guess(guess, answer)):
                break
        except ValueError:
            print('please enter a number')
            continue

