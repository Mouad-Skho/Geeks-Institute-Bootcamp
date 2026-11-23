# Exercise 1 : Dunder Methods

# Output:
# ['a', 'b', 'c']
#
# __repr__ returns str(self.my_list), which is the string
# representation of the list, so print() shows ['a', 'b', 'c'].


# Exercise 2 : Exceptions
my_list = [2, 3, 1, 2, "four", 42, 1, 5, 3, "imanumber"]
total = sum(item for item in my_list if isinstance(item, (int, float)))

print(total)

# Exercise 3 : Writing Our Own Modules
# in Exercise_3

# Exercise 4 : Dogs Domesticated
import sys
from pathlib import Path
import random
sys.path.append(str(Path(__file__).resolve().parents[2]))
from Day1.ExercisesXP.exercises import Dog
class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(super().bark())
        self.trained = True
    def play(self, *args):
        dog_names = ", ".join(dog.name for dog in args)
        print(f"{dog_names} all play together")
    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))


dog1 = PetDog("Buddy", 3, 12)
dog2 = PetDog("Max", 5, 15)
dog3 = PetDog("Bella", 2, 8)

print("-------Day2 Exercise 4----------")
dog1.train()
print("-----------------")
dog1.play(dog2, dog3)
print("-----------------")
dog1.do_a_trick()
print("-----------------")
dog2.do_a_trick()
