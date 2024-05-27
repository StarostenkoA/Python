from abc import ABC, abstractmethod
class Animal (ABC):
    name=''
    
    def __init__(self, name) -> None:
        self.name = name
    
    @abstractmethod
    def says(self):
        pass
    
class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def says (self): 
        return f"{self.name} - Cat. says Meoy!"

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def says (self): 
        return f"{self.name} - Dog. says Gaf!"

class Cow(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def says (self): 
        return f"{self.name} - Cow. says Muu!"

cat=Cat('Mia')
dog=Dog('Sharic')
cow=Cow('Mashka')

print(cat.says())
print(dog.says())
print(cow.says())
