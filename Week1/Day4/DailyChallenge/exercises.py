# Challenge
word = input("input your word: ")
letter_indexes = {}
for (index, letter) in enumerate(word):
    if letter in letter_indexes:
        letter_indexes[letter].append(index)
    else:
        letter_indexes[letter]=[index]
print(letter_indexes)

# Approach and Explanation
# I used input() to ask the user for a word and created an empty dictionary called letter_indexes.
# I used enumerate() to iterate through the word and retrieve both the index and the letter at each position.
# If the letter already exists as a dictionary key, I used .append() to add its new index to the existing list. Otherwise, I created a new key and initialized its value with a list containing the current index.
# This approach ensures that each letter appears only once as a dictionary key, while all its positions are stored in a list.