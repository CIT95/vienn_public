print("Please give me a starting number - only numbers.")
beginning_num = int(input())
print("Please enter the ending number - only numbers.")
ending_num = int(input()) + 1

if beginning_num > ending_num:
    print("The ending of number cannot be greater than the starting number.")
else:
    print("Counting:")
    for i in range(beginning_num, ending_num):
        print(i)
    