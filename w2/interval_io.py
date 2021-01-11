# Getting user to input number
# Line 8 ending_num is + 1 to have the ending number
#  print as an out. Without + 1, it will print one less the
#  the number given.
print("Please give me a starting number - only numbers.") 
beginning_num = int(input())
print("Please enter the ending number - only numbers.")
ending_num = int(input()) + 1 

# if else condition. Starting with a check to verify that the starting number is not
#  greater than the ending number. 
# the else condition will print in range based off the user's input.
if beginning_num > ending_num:
    print("The ending of number cannot be greater than the starting number.")
else:
    print("Counting:")
    for i in range(beginning_num, ending_num):
        print(i)
    