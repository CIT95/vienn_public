# defining the fizz_buzz program
def fizz_buzz(number):
    if number % 15 == 0: #check to see if number is divisible by 5 and 3
        # line 3 can be written as if number % 3 == 0 and number % 5 == 0
        return "FizzBuzz"
    elif number % 5 == 0: #check to see if number is divisible by 5
        return "Buzz"
    elif number % 3 == 0: #check to see if number is divisible 3
        return "Fizz"
    else:
        return number

def getInfo():
    number = int(input("Please enter a number: ")) # getting input from user. needs to be converted to integer.
    print(fizz_buzz(number)) # passes number into fizz_buzz function

getInfo() # running getInfo() will also run fizzBuzz() and give us an output.