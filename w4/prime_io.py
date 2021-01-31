
try: # try block. This is where there can be an error with user's input.
    print("Please give me a starting number - only numbers.")
    beginning_num = int(input())
    print("Please enter the ending number - only numbers.")
    ending_num = int(input()) + 1

except ValueError: # what to do if we get a ValueError
    print('Please only enter numerical values.')

else: # If the input is good, do this
    if beginning_num > ending_num:
        print("The ending of number cannot be greater than the starting number.")
    else:
        print("Counting:")
        for num in range(beginning_num, ending_num + 1):
            if num > 1:
                for i in range(2, num // 2):
                    if (num % i) == 0:
                        break
                else:
                    print(num)

finally: # Using finally was a way to alway print a thank you note.
    print(f'\nThank you for running this program!') 