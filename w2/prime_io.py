print("Please give me a starting number - only numbers.")
beginning_num = int(input())
print("Please enter the ending number - only numbers.")
ending_num = int(input()) + 1

if beginning_num > ending_num:
    print("The ending of number cannot be greater than the starting number.")
else:
    print("Counting:")
    for i in range(beginning_num, ending_num):
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0: 
            print(i)
        elif i == 2 or i == 3 or i == 5 or i == 7:
            print(i) # telling python that if i is 2, print it.

