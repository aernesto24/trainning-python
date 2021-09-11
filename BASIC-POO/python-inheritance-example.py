#This is Basic inheritance example from Platzi trainning courses

class Rectangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height

    
    def area(self):
        return self.base * self.height


#The following statement is similar in concept to extend on other languages
class Square(Rectangle):

    def __init__(self, side):
        #super() allows to obtain a reference from the superclass
        #in this case Rectangle
        super().__init__(side, side)


if __name__ == "__main__":

    base = int(input('Define the base: '))
    height = int(input('Define the height: '))

    rectangle = Rectangle(base, height)
    print(f'The area for the rectangle is {rectangle.area()}')

    side = int(input('Define the side value: '))
    square = Square(side)
    print(f'The are for the square is {square.area()}')
    