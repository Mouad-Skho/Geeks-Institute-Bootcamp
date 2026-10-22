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