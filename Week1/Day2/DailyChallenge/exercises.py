# Challenge 1
number = int(input("Enter a number: "))
length = int(input("Enter a length: "))
list_of_multiples =[]
for i in range(1, length+1):
    list_of_multiples.append(number*i) 
print(list_of_multiples)
# Challenge 2
word = "letter"
print(set(word))
