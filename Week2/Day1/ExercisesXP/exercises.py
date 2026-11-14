# Exercise 1 : Pets
class Pets():
    def __init__(self, animals):
        self.animals = animals
    def walk(self):
        for animal in self.animals:
            print(animal.walk())
class Cat():
    is_lazy = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def walk(self):
        return f'{self.name} is just walking around'
class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'
class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'
all_cats = [Bengal('Randy', 1),Chartreux('Karela', 2),Siamese('Sam', 3)]
sara_pets = Pets(all_cats)
sara_pets.walk()

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

# Exercise 3 : Family
class Family():
    def __init__(self, last_name, members):
        self.members = members
        self.last_name = last_name
    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations! {self.last_name} family has a new member: {kwargs}")
    def is_18(self, name):
        for member in self.members:
            if member["name"] == name:
                return member["age"] >= 18
    def family_presentation(self):
        print(f"Family {self.last_name} members:")
        for member in self.members:
            print(f"{member['name']} is {member['age']} years old, {member['gender']} and {'a child' if member['is_child'] else 'an adult'}")
    
family1 =Family(
    last_name="Zitouni",
    members=[
    {'name':'l3arbi','age':35,'gender':'Male','is_child':False},
    {'name':'Rahma','age':32,'gender':'Female','is_child':False}
]
)
family1.family_presentation()
print("-----------------")

family1.born(name="3alal", age=10, gender="Male", is_child=True)
print("-----------------")
family1.family_presentation()
print("-----------------")
print(family1.is_18("l3arbi"))
print(family1.is_18("Rahma"))
print(family1.is_18("3alal"))
print("-----------------")

# Exercise 4 : TheIncredibles Family
class TheIncrediblesFamily(Family):
    def __init__(self, last_name, members):
        super().__init__(last_name, members)
    def use_power(self):
        for member in self.members:
            if member["age"] >= 18:
                print(f"{member['incredible_name']} is using {member['power']}")
            else:
                print(f"{member['name']} is too young to use their power.")
    def incredible_presentation(self):
        print("Here is our powerful family")
        super().family_presentation()
theIncredibles = TheIncrediblesFamily(
    last_name="Zitouni",
    members=[    
        {'name':'l3arbi','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
        {'name':'Rahma','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
]
)
theIncredibles.incredible_presentation()
print("-----------------")
theIncredibles.use_power()
print("-----------------")
theIncredibles.born(name="3alal", age=10, gender="Male", is_child=True, power="Unknown Power", incredible_name="3alalFly")
print("-----------------")
theIncredibles.incredible_presentation()
print("-----------------")
theIncredibles.use_power()
