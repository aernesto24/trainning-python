#This is Basic Polymorphism example from Platzi trainning courses
class Person:
    
    def __init__(self, name):
        self.name = name

    def move(self):
        print('I am walking')

    
#A person walks but this is not always true, what happens if it is a cyclist for example
class Cyclist(Person):

    def __init__(self, name):
        #pass the parameters that init requires from the superclass
        super().__init__(name)

    def move(self):
        print('I am moving on a biclycle')


def run():
    person = Person('Ernest')
    person.move()

    cyclist = Cyclist('Pablo')
    cyclist.move()


if __name__ == '__main__':
    run()

