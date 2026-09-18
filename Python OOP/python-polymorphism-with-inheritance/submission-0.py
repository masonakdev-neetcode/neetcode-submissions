class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def make_sound(self) -> None:
        print("Animal is making a sound")


class Dog(Animal):
    def make_sound(self) -> None:
        print(f"{self.name} says: Woof!")
    

class Cat(Animal):
    def make_sound(self) -> None:
        print(f"{self.name} says: Meow!")

def do_animal_stuff(animal: Animal) -> None:
    animal.make_sound()

animal = Animal("Rabbit")
do_animal_stuff(animal)

animal = Dog("Buddy")
do_animal_stuff(animal)

animal = Cat("Whiskers")
do_animal_stuff(animal)
