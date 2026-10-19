# Exercise 1: What is the Season?
from operator import index

month = int(input("What is the month? "))
if month in range(1,13):
    if month in range(3,5):
        print("Spring")
    elif month in range(6,8):
        print("Summer")
    elif month in range(9,11):
        print("Autumn")
    elif month in [12,1,2]:
        print("Winter")

else:
    print("type a valid month bettwen 1 to 12 ")
# Exercise 2: For Loop
# Q1
for i in range(1,21):
    print(i)
# Q2
for i in range(1,21):
    if i % 2 == 0:
        print(i)
# Exercise 3: While Loop
name = input("What's your name? ").lower()
ref = "mouad"
while name != ref:
    print("try again")
    name = input("What's your name? ").lower()
# Exercise 4: Check the index
print("welcome")
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
checkword = input("enter the word: ")
if checkword in names:
    print(names.index(checkword))
else:
    print("The word is not in the list.")
# Exercise 5: Greatest Number
number1 = int(input("What is the 1st number? "))
number2= int(input("What is the 2nd number? "))
number3 = int(input("What is the 3rd number? "))

if number1 > number2 and number1 > number3 :
    greatest = number1
elif number2 > number1 and number2 > number3 :
    greatest = number2
else:
    greatest = number3
print("The Greatest number is: " + str(greatest))

# Exercise 6: Random number
import random
win = 0
losses = 0
correct_number =random.randrange(1, 10)
while True:
    number = int(input("Guess a number between 1 and 9 (or 0 to quit): "))
    if number == 0:
        print(f"Game over! You won {win} games and lost {losses} games.")
        break
    elif number < 1 and number > 9 :
        print("Type a valid number bettwen 1 and 9")
    elif correct_number == number :
        print("Winner!")
        win += 1
        correct_number =random.randrange(1, 10)
    else :
        print("Better luck next time.") 
        losses += 1
    
    
