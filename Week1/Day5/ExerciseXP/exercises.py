#  Exercise 1: Cats
# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
# cat1= Cat("meow",2)
# cat2= Cat("woem",1)
# cat3= Cat("omew",3)
# def oldest_cat(cat1,cat2,cat3):
#     if cat1.age > cat2.age and cat1.age > cat3.age:
#         oldstcat = cat1
#     elif cat2.age > cat1.age and cat2.age > cat3.age:
#         oldstcat = cat2
#     else:
#         oldstcat = cat3
#     print(f"The oldest cat is {oldstcat.name}, and is {oldstcat.age} years old.")
# oldest_cat(cat1,cat2,cat3)



# Exercise 2 : Dogs
# class Dog:
#     def __init__(self, name,height):
#         self.name = name
#         self.height = height
#     def bark(self):
#         print(f"{self.name} goes woof!")
#     def jump(self):
#         print(f"{self.name} jumps {self.height * 2} cm high!")
# dog =Dog('test',12)
# davids_dog =Dog('Rex',50)
# sarahs_dog =Dog('Teacup',20)
# davids_dog.bark()
# davids_dog.jump()
# sarahs_dog.bark()
# sarahs_dog.jump()
# if sarahs_dog.height > davids_dog.height :
#     print("Teacup is bigger")
# else:
#     print("Rex is bigger")

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