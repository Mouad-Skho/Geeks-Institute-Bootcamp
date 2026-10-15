keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
res = {key: value for key, value in zip(keys, values)}
print(res)
# Exercise 2 : Cinemax #2

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
    
    