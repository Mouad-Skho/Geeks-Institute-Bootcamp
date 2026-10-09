#Exercise 1 : Hello World
print("Hello world \n" * 4)
#Exercise 2 : Some Math
print(99**3*8)
#🌟 Exercise 3 : What’s your name ?
name = input("What's your name? ")
if name.lower() == "mouad":
    print("Wait... we're twins!")
else:
    print(f"Nice to meet you, {name}! But sadly, you're not me.")
#Exercise 4 : Tall enough to ride a roller coaster
height = float(input("What is your height in centimeters? "))
if height > 145:
    print("You are tall enough to ride.")
elif height < 145:
    print("You need to grow some more to ride.")
#Exercise 5 : Favorite Numbers
my_fav_numbers = {1, 2, 3, 4}
my_fav_numbers.add(5)
my_fav_numbers.add(6)
my_fav_numbers.remove(6)
print(my_fav_numbers)

friend_fav_numbers = {7,8,9,0}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)
#Exercise 6: Tuple
#No, you cannot add more integers directly to a tuple because tuples are immutable in Python, meaning their values cannot be changed after creation.
# Exercise 7: List
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("kiwi")
basket.append("Apples")
basket.count("Apples")
basket.clear()
print(basket)
# Exercise 8 : Sandwich Orders
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
print(sandwich_orders)

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders[0]
    finished_sandwiches.append(sandwich)
    sandwich_orders.remove(sandwich)
    print("I made your " + sandwich.lower())

