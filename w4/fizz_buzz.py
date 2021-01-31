def fizz_buzz(number):
    """
    return FizzBuzz, Buzz, or Fizz if the user number is divisble by 15, 5 or 3
    """
    if number % 15 == 0: 
        return "FizzBuzz"
    elif number % 5 == 0: 
        return "Buzz"
    elif number % 3 == 0: 
        return "Fizz"
    else:
        return number

def getInfo():
    """
    get user's input
    """
    try:
        number = int(input("Please enter a number: "))
        if number == 111:
            raise Exception 
    except ValueError: # alerting user to enter a numberical number
        print('Please enter a numerical value.')
        SystemExit
    except Exception:
        print("That's the magic number!")
        print(fizz_buzz(number))
    else: # if the try block is true, thank you the user and run the fizz_buzz()
        print("Thank you for entering numerical value!")
        print(fizz_buzz(number)) # passes number into fizz_buzz function
    finally:
        print("Thank you for running this program.")
    

getInfo() # running getInfo() will also run fizzBuzz() and give us an output.