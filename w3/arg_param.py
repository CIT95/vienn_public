def weeklyPay(wage, hours= 40): # two parameters, hours is set to default at 40
    pay = wage * hours #set the weekly pay to a variable
    print(
        "Working " + str(hours) + " hours a week at $" + str(format(wage, '.2f')) + 
        " per hour, your TOTAL weekly pay is $" + str(format(pay, '.2f')) + 
        " dollars. (Taxes not included)") #prints the total pay, hours worked, and hour rate

def getWage():
    #get hourly wage
    wage = float(input("What is your current hourly wage? ")) 
    #get numbers of hour worked a week
    hoursPerWeek = int(input(f"How many hours do you work a week?\n(If you're unsure enter 0): "))
    
    if hoursPerWeek == 0: #if user enter 0, we will use the default value of 40 hours
        weeklyPay(wage) #calling weeklyPay with wage only.
    else:
        weeklyPay(wage, hoursPerWeek) #using both user inputs. Not using default value.

#running the getWage().
getWage() 

#running weeklyPay() without an hours agrument. Default value of 40 would be used.
print(f"\nThe following output is when we run: weeklyPay(15.75) which will use the default value")
weeklyPay(15.75) 