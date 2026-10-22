#  Exercise 1: Cats
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
cat1= Cat("meow",2)
cat2= Cat("woem",1)
cat3= Cat("omew",3)
def oldest_cat(cat1,cat2,cat3):
    if cat1.age > cat2.age and cat1.age > cat3.age:
        oldstcat = cat1
    elif cat2.age > cat1.age and cat2.age > cat3.age:
        oldstcat = cat2
    else:
        oldstcat = cat3
    print(f"The oldest cat is {oldstcat.name}, and is {oldstcat.age} years old.")
oldest_cat(cat1,cat2,cat3)



# Exercise 2 : Dogs
class Dog:
    def __init__(self, name,height):
        self.name = name
        self.height = height
    def bark(self):
        print(f"{self.name} goes woof!")
    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")
dog =Dog('test',12)
davids_dog =Dog('Rex',50)
sarahs_dog =Dog('Teacup',20)
davids_dog.bark()
davids_dog.jump()
sarahs_dog.bark()
sarahs_dog.jump()
if sarahs_dog.height > davids_dog.height :
    print("Teacup is bigger")
else:
    print("Rex is bigger")

# Exercise 3 : Who’s the song producer
class Song:
    def __init__(self,lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for i in self.lyrics:
            print(i)
            print('\n')
stairway= Song(["There's a lady who's sure","all that glitters is gold", "and she's buying a stairway to heaven"])
stairway.sing_me_a_song()

# Exercise 4 : Afternoon at the Zoo
class Zoo:
    def __init__(self,zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
    def add_animal(self,new_animal):

        if new_animal not in self.animals:
            self.animals.append(new_animal)
    def get_animals(self):
        for i in self.animals:
            print(i)
    def sell_animal(self,animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
    def sort_animals(self):
        self.animals.sort()
        group = {}
        for animal in self.animals:
            letter = animal[0].upper()
            if letter in group:
                group[letter].append(animal)
            else:
                group[letter] = [animal]
        return group
    def get_groups(self):
        groups = self.sort_animals()
        for letter,animal in groups.items():
            print(letter,":",animal)

ain_sbaa_zoo = Zoo("New York Zoo")
while True:
    animal = input("Which animal should we add to the zoo? (type 'done' to finish): ")
    if animal.lower()== 'done':
        break
    else:
        ain_sbaa_zoo.add_animal(animal)


ain_sbaa_zoo.add_animal("Giraffe")
ain_sbaa_zoo.add_animal("Bear")
ain_sbaa_zoo.add_animal("Baboon")
ain_sbaa_zoo.add_animal("Cat")
ain_sbaa_zoo.add_animal("Cougar")
ain_sbaa_zoo.add_animal("Ape")
ain_sbaa_zoo.add_animal("Elephant")
ain_sbaa_zoo.add_animal("Eel")
ain_sbaa_zoo.add_animal("Emu")
ain_sbaa_zoo.add_animal("Lion")
ain_sbaa_zoo.add_animal("Leopard")
ain_sbaa_zoo.add_animal("Tiger")
ain_sbaa_zoo.add_animal("Zebra")
ain_sbaa_zoo.add_animal("Monkey")


ain_sbaa_zoo.get_animals()
print("------------------------")
ain_sbaa_zoo.add_animal("Giraffe")  
ain_sbaa_zoo.sell_animal("Bear")    
ain_sbaa_zoo.sell_animal("Panda")   

ain_sbaa_zoo.sort_animals()
ain_sbaa_zoo.get_animals()
print("------------------------")
ain_sbaa_zoo.get_groups()