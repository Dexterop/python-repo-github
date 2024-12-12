class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Arff! Arff! Arff!")
    
d= Dog()
d.bark()