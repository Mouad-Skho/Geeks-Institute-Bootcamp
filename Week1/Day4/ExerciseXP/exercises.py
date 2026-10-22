keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
res = {key: value for key, value in zip(keys, values)}
print(res)
# # Exercise 2 : Cinemax #2
family ={}
total_cost = 0
member =int(input("Welcome to Cinemax, how many family members: "))
for i in range(member):
    print("--------- membre : " + str(i+1) +" ---------")
    name = input("input the name: ")
    age = int(input("input the age: "))
    while age < 0:
        print("Enter a valid age")
        age = int(input("Input the age: "))
    family[name] = age
for x, y in family.items():
    if y < 3 :
        total_cost = total_cost + 0
    elif y >= 3 and y <= 12 :
        total_cost = total_cost + 10
    elif y > 12 :
        total_cost = total_cost + 15
print(family)
print(total_cost)
# Exercise 3: Zara
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

brand["number_stores"] = 2
for i in brand["type_of_clothes"]:
    print(i)
brand["country_creation"]="Spain"
if "international_competitors" in brand :
    brand["international_competitors"].append("Desigual")
del brand["creation_date"]
print(brand["international_competitors"][-1])
print(brand["major_color"]["US"])
print(len(brand))
for x in brand:
    print(x + "\n")

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000,
}
brand.update(more_on_zara)

print(brand["number_stores"])

# Exercise 4 : Some Geography
def describe_city(city , country = "maroc"):
    return print(f"{city} is in {country}")
describe_city("casablanca")

# Exercise 5 : Random
import random
def random_generate(number):
    random_number = random.randint(1,100)
    if random_number == number :
        return print("success message")
    else:
        return print(f"fail message: your number in {number} and the random number is {random_number}")
random_generate(14)
# Exercise 6 : Let’s create some personalized shirts !
def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}")
make_shirt("large","Keep Life Simple")
make_shirt()
make_shirt("medium")
make_shirt("small", "Python is fun")
make_shirt(text="Keep Learning", size="medium")
#  Exercise 7 : Temperature Advice
import random
def get_random_temp(season):
    if season.lower() == "winter" or season in str([12,1,2]):
        upper = 16
        lower = 10
    elif season.lower() == "spring" or season in str(range(3,5)):
        upper = 25
        lower = 0
    elif season.lower() == "summer" or season in str(range(6,8)):
        upper = 40
        lower = 16
    elif season.lower() == "autumn" or season in str(range(9,11)):
        upper = 30
        lower = 0
        
    temp = random.randint(lower,upper)
    return temp
print(get_random_temp("Autumn"))
def main():
    while True:    
        season_in = input("Please enter a season (winter, spring, summer, or autumn): ")
        if season_in in ["winter","spring","summer","autumn"] or range(1,13) :
            season_out = season_in
            print(season_out)
            break
        else :
            print("enter a valid Season")
    
    temp = get_random_temp(season_out)
    print(f"The temperature right now is {temp} degrees Celsius")
    if temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif temp >= 0 and temp < 16:
        print("Quite chilly! Don't forget your coat.")
    elif temp >= 16 and temp <= 23:
        print("The weather is mild! A light jacket might be a good idea.")
    elif temp >= 24 and temp <= 32:
        print("It's warm outside! Perfect weather for a T-shirt.")
    elif temp >= 33 and temp <= 40:
        print("It's really hot! Stay hydrated and wear light clothing.")
main()

# Exercise 8 : Star Wars Quiz

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]
def ask_questions():
    correct_answers = 0
    incorrect_answers = 0
    wrong_answers = []
    for item in data:
        print(item["question"])
        user_answer = input("Your answer: ")
        if user_answer.lower() == item["answer"].lower():
            correct_answers += 1
        else:
            incorrect_answers += 1
            wrong_answers.append({"question":item['question'],"answer":item['answer'],"user_answer":user_answer})
    return correct_answers,incorrect_answers,wrong_answers
def show_results():
    correct_answers,incorrect_answers,wrong_answers = ask_questions()
    print(f"The number of correct answers: {correct_answers}")
    print(f"The number of incorrect answers: {incorrect_answers}")
    print(f"The incorrect answers is:")

    for i in wrong_answers:
        print("-----------------------------")
        print(f"The Question is: {i['question']} ")
        print(f"Your Answer: {i['user_answer']} ")
        print(f"The correct answer: {i['answer']} ")
    if incorrect_answers > 3 :
        play_again = input("Game over to play again tab 'yes': ")
        if play_again.lower() == "yes":
            ask_questions()
        


show_results()