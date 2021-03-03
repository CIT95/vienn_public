import random

user_string = input("Please input a string: ")

# First Challenge: (MEDIUM)
# Write a Python function to reverses a string if it's length is a multiple of 4.
# Needed to look up how to reverse a string. Was going to make the string into
# a list and reverse the list, but there's a simpler way: slice it [::-1].
def reverse_string(user_string):
    if len(user_string) % 4 == 0:
        # Slice from the end of the string and move backwards to print reverse
        return user_string[::-1]
    return user_string
print("The user's string, if its length is a multiple of four, is: ")
print(reverse_string(user_string))
# Alternate way to print reverse string is:
# return ''.join(reversed(str1))

# Second Challenge (VERY HARD)
# Write a Python program to create a Caesar encryption.

# Problems that needs to be solved: 1) how to convert the letter to a number.
# 2) how to add/shift the number 3) how to print the encrypted word.
# learned that ord() is a built in function to find ASCII number of string.
# i had to look this up, but even then, is still didn't solve it.
# i learned about chr() and ord() and how the convert unicode to a number. 
# theoretically, we can get all the numbers for the string, add the shift to it
# and then use chr() on the numbers to get a new, encrypted string. 

# This solution is form https://www.thecrazyprogrammer.com/2018/05/caesar-cipher-in-python.html
# This program did exactly how I thought the process should work. The pieces I was missing is the
# use of a modulus and the additional mathetical parts.
def encrypt(string, shift):
 
  cipher = '' 
  for char in string: 
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65) 
    else:
      cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
  
  return cipher

# My Solution:
# text = input("enter string: ")
# s = int(input("enter shift number: "))
# print("original string: ", text)
# print("after encryption: ", encrypt(text, s))
# def caesar_encryption(user_string):
#     encrypted_string = []
#     for letter in user_string:
#         number = ord(letter) - 96
#         encrypted_string.append(chr(number + 7))
#     return encrypted_string      
# print(caesar_encryption(user_string))
        
# Third Challenge (HARD) was not sucessful.
# Given two strings, s1 and s2, create a mixed String.
#Note: create a third-string made of the first char of s1 then the last char 
# of s2, Next, the second char of s1 and second last char of s2, and so on. 
# Any leftover chars go at the end of the result.
# s1 = "Abc" s2 = "Xyz" --> AzbycX
s1 = "Abc"
s2 = "Xyz"

def new_s3(s1, s2):
    s3 = []
    for i in word:
        s3.append()

# Solution:
def mixString(s1, s2):
  s2 = s2[::-1]  # just learn that [::-1] is a way to reverse the string
  lengthS1 = len(s1)
  lengthS2 = len(s2)
  length  = lengthS1 if lengthS1 > lengthS2 else lengthS2 
  resultString=""
  # Loop through, adding one s1 characer, the add one char from s2, creating a new string
  for i in range(length): 
    if(i < lengthS1):
      resultString = resultString + s1[i]
    if(i < lengthS2):
      resultString = resultString + s2[i]
    
  print(resultString)
  
s1 = "Abc"
s2 = "Xyz"
mixString(s1, s2)

# Fourth Challenge: (MEDIUM)
# Find all occurrences of “USA” in given string ignoring the case.
# Expected outcome: "The USA count is: 2."
str1 = "Welcome to USA. usa awesome, isn't it?"
str1 = str1.lower()

# Solution:
inputString = "Welcome to USA. usa awesome, isn't it?"
substring = "USA"
tempString = inputString.lower()
count = tempString.count(substring.lower()) # .count() method was used
                                            # to find how many substring
                                            #was in the main string.
print("The USA count is:", count)

# Fifth Challenge: (MEDIUM) SOLVED SOLO
# Given a string of odd length greater 7, return a string made of the middle three chars of a given String
# str1 = "JhonDipPeta" --> 'Dip'
str1 = "JhonDipPeta"
new_str = str1[(int((len(str1))/2) - 1):(int((len(str1))/2) + 2)]
print(new_str)
#Solution from website
def getMiddleThreeChars(sampleStr):
  middleIndex = int(len(sampleStr) /2)
  print("Original String is", sampleStr)
  middleThree = sampleStr[middleIndex-1:middleIndex+2]
  print("Middle three chars are", middleThree)
  
getMiddleThreeChars("JhonDipPeta")
getMiddleThreeChars("Jasonay")

# Sixth Challenge EASY! Solved solo
# Write a Python program to calculate the length of a string. 
# my solution:
string_length = len(user_string)
print(f"The user string: {user_string} has a length of {string_length}.")
# solution from the website:
def string_length(str1):
    count = 0
    for char in str1:
        count += 1
    return count
#looks like they used a loop and used a variable to keep count.

# Seventh Challenge (MEDIUM)
# Split a given string on hyphens into several substrings and display each 
# substring

# Solution:
str1 = "Emma-is-a-data-scientist"
print("Original String is:", str1)

# split string
substrings = str1.split("-") #using .split() to remove the '-'.

print("Displaying each substring") # using a loop to print out the strings
for sub in substrings:
    print(sub)

# Eigth Challenge EASY. No help needed for this one.
# Write a Python script that takes input from the user and displays that input
# back in upper and lower cases
print(f"User string as uppercase: {user_string.upper()}.")
print(f"User string as lower case: {user_string.lower()}.")

# Ninth Challenge: (MEDIUM) looks like another solutiont that used .split() method. DID NOT solve on my own.
# Write a Python program that accepts a comma separated sequence of words as 
# input and prints the unique words in sorted form (alphanumerically).
user_list = input("Enter some words separated by a comma and will return it sorted: ")
li = list(user_list)
print(user_list)
print(li)
# Solution:
items = input("Input comma separated sequence of words")
words = [word for word in items.split(",")] #interesting way to do a loop
print(",".join(sorted(list(set(words)))))

# Tenth Challenge EASY - SOLVED SOLO
# Write a Python function to get a string made of its first three characters 
# of a specified string. If the length of the string is less than 3 then 
# return the original string
# No help needed for this one.
if len(user_string) > 3:
  print(user_string[:3])
else:
  print("The string is less than characters.")
# Solution: The solution used less lines of codes. is more efficient than mine.
def first_three(str):
	return str[:3] if len(str) > 3 else str

print(first_three('ipy'))
print(first_three('python'))
print(first_three('py'))