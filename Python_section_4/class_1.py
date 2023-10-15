#OOP
class PlayerCharacter:
    # Class object attribute (static)
    membership = True
    def add( num3, num4 ):
        return num3 + num4
    
    def __init__( self, name, age ):
        self._name = name
        self.age = age
        self.attack = 50

    def run( self ):
        print('run')

    def speakAge( self ):
        print(f'name: {self._name}, Speaks: {self.age}')

    @classmethod # use cls only with @classmethod
    def adding_things(cls, num1, num2 ):
        return cls( "Tom", num1 + num2 )
    
    @classmethod # use cls only with @classmethod
    def return_cls( cls ):
        return cls
    
    @staticmethod # we dont have access to cls in @staticmethod
    def adding_things2(num1, num2 ):
        return num1 + num2
    

Player1 = PlayerCharacter( "Nick", 30 )
Player2 = PlayerCharacter( "Tom", 28 )

Player1.speakAge()
Player2.speakAge()

print(len((1,2,3)))

Player1.speak = 9000
Player1.name = 'Sasha'

print(Player1.speak)

Player1.speakAge()

