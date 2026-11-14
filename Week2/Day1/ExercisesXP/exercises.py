# Exercise 1 : Pets
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())


# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'


# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'


# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
# class Siamese(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
# all_cats = [Bengal('Randy', 1),Chartreux('Karela', 2),Siamese('Sam', 3)]
# sara_pets = Pets(all_cats)
# sara_pets.walk()

# Exercise 2 : Dogs
class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self):
        return f'{self.name} is barking'
    def run_speed(self):
        return f'the {self.name} running speed: {self.weight / self.age * 10}'
    def fight(self, other_dog):
        if self.run_speed()*self.weight > other_dog.run_speed()*other_dog.weight:
            return f'{self.name} wins the fight!'
        else:
            return f'{other_dog.name} wins the fight!'

dog1 = Dog('Rex', 2, 10)
dog2 = Dog('Fido', 3, 15)
dog3 = Dog('Spot', 4, 12)

print(dog1.run_speed())
print(dog2.run_speed())
print(dog3.run_speed())

print(dog1.fight(dog2))
print(dog2.fight(dog1))
print(dog3.fight(dog2))
print(dog1.fight(dog3))