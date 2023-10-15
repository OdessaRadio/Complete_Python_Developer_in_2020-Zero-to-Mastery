class User:
    def __init__(self):
        print("User call")

    def sign_in(self):
        print('logged in')



class Archer(User):
    def __init__(self, name, num_arrows = 30):
        self.name = name
        self.num_arrows = num_arrows
        print('Archer call')
    
    def shoot(self):
        self.num_arrows -= 1
        print(f'{self.name} attacking with arrows. Number of arrows left: {self.num_arrows}')

    def run(self):
        print(f'Archer {self.name} is running')

class Wizard(User):
    def __init__(self, name, power = 15):
        self.name = name
        self.power = power
        print('Wizard call')

    def attack(self):
        print(f'{self.name} attacking with power of {self.power}')

    def check_errors(self):
        print(f'Wizard {self.name} checks errors')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


wizard1  = Wizard('Merlin', 25)
archer1 = Archer('Robin',100)
hb1 = HybridBorg('borgie', 50, 100)

#hb1.check_errors()
hb1.check_errors() # Diamond inheritance 
hb1.shoot()
hb1.sign_in()

'''
METHOD RESOLUTION ORDER (MRO) in both the declaration style is different. 
Old style classes use DLR or DEPTH-FIRST LEFT TO RIGHT algorithm whereas new style classes use C3 Linearization algorithm 
for method resolution while doing multiple inheritances. 
'''