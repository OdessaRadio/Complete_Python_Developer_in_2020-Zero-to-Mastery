class User:
    def __init__(self, name, email):
        print(f'{self.__class__} class call')
        self.name = name
        self.email = email

    def sign_in(self):
        print('logged in')

    #interface function, overloaded in child classes
    def attack(self):
        print('do nothing')

    def show_email(self):
        print(f'{self.name} email is: {self.email}')

class Wizard(User):
    def __init__(self, name, email, power = 15):
        print(f'{self.__class__} class call')
        super().__init__(name, email) # -> super().__init__(name, email)
        self.power = power

    def attack(self):
        print(f'{self.name} attacking with power of {self.power}')

    #def show_email(self):
    #    print(f'{self.name} email is: {self.email}')

class Archer(User):
    def __init__(self, name, email, num_arrows = 50):
        print(f'{self.__class__} class call')
        super().__init__(name, email) # -> super().__init__(name, email)
        self.num_arrows = num_arrows
    
    def attack(self):
        print(f'{self.name} attacking with arrows. Number of arrows left: {self.num_arrows}')
        self.num_arrows -= 1
    
    #def show_email(self):
    #    print(f'{self.name} email is: {self.email}')

wizard1  = Wizard('Merlin', 'merlin@gmail.com', 25)
archer1 = Archer('Robin','robin@gmail.com', 100)

def player_attack(char : User):
    char.attack()

def show_e(char : User):
    char.show_email()

#print( isinstance(wizard1, object) )
#print( isinstance(list, object) )

wizard1.sign_in()

player_attack(wizard1)
player_attack(archer1)

show_e(wizard1)
show_e(archer1)

print(wizard1.email)


# introspection - ability to determine the object type during runtime
print(dir(wizard1))