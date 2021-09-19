# All solutions to the Coding Challenge are written in Python 3.9.


# Write a program that checks if 15 is divisible by 3. 
# If it is divisible, the program prints True and if it is not divisible, then we print False.

# number = 15

# if number % 3 == 0:
#     print(True)
# else:
#     print(False)


# Create a list of 5 animals. Print each animal in the list one by one using a for loop.

# animals = ["Aardvark", "Elephant", "Horse", "Pig", "Cow"]

# for animal in animals:
#     print(animal)


# Store the total of the following integers in a variable: 10, 20, 34 and 13. 
# Print the total using the print function.

# sum = 10 + 20 + 34 + 13
# print(sum)


# Continuously generate and print random integers in the range 1 to 20 until 14 is generated. 
# The integer 14 should also be printed at the end.

# from random import randint

# while (number := randint(1, 20)) != 14:
#     print(number)


# Write a program that uses a for loop to print from 10 to -5 and prints "Complete" once at the end.

# for number in range(10, -6, -1):
#     print(number)

# print("Complete")


# Create an empty list. Append random odd integers in the range 1 to 50 to the list until the list contains 10 integers. 
# Print the list along with its length.

# from random import randrange

# numbers = []
# numbers = [randrange(1, 51, 2) for _ in range(10)]

# print(numbers, len(numbers))


# Write a function that uses the random module to simulate a coin toss and 
# returns either "Heads" or "Tails". Call the function and print the returned value.

# from random import randint


# def flip():
#     return "Heads" if randint(0, 1) else "Tails"


# print(flip())


# Write a program that uses for loop(s) to print integers from 1 to 5 and then back to 1 in the same line.
# Tip: Use end argument, string concatenation or any other logic of your choice.
# Expected output: 123454321

# for number in range(1, 6):
#     print(number, end="")

# for number in range(4, 0, -1):
#     print(number, end="")


# Ask the user to enter 10 words one by one. If the entered word contains at least two different vowels, then put the word into a text file named "words.txt".
# Tip: The letters 'a', 'e', 'i', 'o', and 'u' are considered vowels.

# words = [input("Enter a word: ") for _ in range(10)]

# with open("words.txt", "w") as words_file:
#     for word in words:
#         if len({"a", "e", "i", "o", "u"} & set(word.lower())) >= 2:
#             print(word, file=words_file)


#


# Create a 2D list of of length 4 with each inner list containing the First Name and Last Name as two separate elements. 
# Use a loop to find and print the longest full name. 
# If there are multiple such names, print all of them in different lines.
# Example: [['John', 'Stuart'], ['Alice', 'Goldman'], ['Mike', 'Smith'], ['Hannah', 'Johnson']]
# Output: HannahJohnson

# names = [['John', 'Stuart'], ['Alice', 'Goldman'], ['Mike', 'Smith'], ['Hannah', 'Johnson']]
# names = ["".join(name) for name in names]
# longest_length = max(len(name) for name in names)
# [print(name) for name in names if len(name) == longest_length]


# Create a list as shown below.
# fruits = ["Apple", "Banana", "Pear", "Apple", "Pineapple", "Apple", "Pear", "Guava", "Grapes", "Watermelon"]
# Generate a dictionary that contains the fruits in the list as keys and the number of time they are in the list as the values. Print the dictionary.
# Tip: To find the number of times Apple occurs in the list, use the below syntax:
# fruits.count('Apple')

# fruits = ["Apple", "Banana", "Pear", "Apple", "Pineapple", "Apple", "Pear", "Guava", "Grapes", "Watermelon"]
# print({fruit: fruits.count(fruit) for fruit in fruits})

