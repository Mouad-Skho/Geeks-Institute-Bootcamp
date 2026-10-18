# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# res = {key: value for key, value in zip(keys, values)}
# print(res)
# # Exercise 2 : Cinemax #2

# family ={}
# total_cost = 0
# member =int(input("Welcome to Cinemax, how many family members: "))
# for i in range(member):
#     print("--------- membre : " + str(i+1) +" ---------")
#     name = input("input the name: ")
#     age = int(input("input the age: "))
#     while age < 0:
#         print("Enter a valid age")
#         age = int(input("Input the age: "))
#     family[name] = age
# for x, y in family.items():
#     if y < 3 :
#         total_cost = total_cost + 0
#     elif y >= 3 and y <= 12 :
#         total_cost = total_cost + 10
#     elif y > 12 :
#         total_cost = total_cost + 15
# print(family)
# print(total_cost)
# Exercise 3: Zara
# brand = {
#     "name": "Zara",
#     "creation_date": 1975,
#     "creator_name": "Amancio Ortega Gaona",
#     "type_of_clothes": ["men", "women", "children", "home"],
#     "international_competitors": ["Gap", "H&M", "Benetton"],
#     "number_stores": 7000,
#     "major_color": {
#         "France": "blue",
#         "Spain": "red",
#         "US": ["pink", "green"]
#     }
# }

# brand["number_stores"] = 2
# for i in brand["type_of_clothes"]:
#     print(i)
# brand["country_creation"]="Spain"
# if "international_competitors" in brand :
#     brand["international_competitors"].append("Desigual")
# del brand["creation_date"]
# print(brand["international_competitors"][-1])
# print(brand["major_color"]["US"])
# print(len(brand))
# for x in brand:
#     print(x + "\n")

# more_on_zara = {
#     "creation_date": 1975,
#     "number_stores": 10000,
# }
# brand.update(more_on_zara)

# print(brand["number_stores"])

# Exercise 4 : Some Geography
# def describe_city(city , country = "maroc"):
#     return print(f"{city} is in {country}")
# describe_city("casablanca")

# Exercise 5 : Random
# import random
# def random_generate(number):
#     random_number = random.randint(1,100)
#     if random_number == number :
#         return print("success message")
#     else:
#         return print(f"fail message: your number in {number} and the random number is {random_number}")
# random_generate(14)
# Exercise 6 : Let’s create some personalized shirts !
def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}")
make_shirt("large","Keep Life Simple")
make_shirt()
make_shirt("medium")
make_shirt("small", "Python is fun")
make_shirt(text="Keep Learning", size="medium")