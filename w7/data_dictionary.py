import pprint # importing pprint to print nicely.
import statistics # to use the mean() 

# create a dd and add keys and values to it. 
# initialized dicitonary
miles_ran_per_day = {
    'Monday': 10, 
    'Tuesday': 5, 
    'Wednesday': 6, 
    'Thursday': 10, 
    'Friday': 10, 
    'Saturday': 1, 
    'Sunday':14
}

# sorting the data in ascending order by the value which is the number of miles ran.
sorted_miles_ran_per_day = sorted(miles_ran_per_day.items(), key=lambda x: x[1])

# using pprint to print in each key by itself. Easier to read.
print("Outputing the sorted values using pprint():")
pprint.pprint(sorted_miles_ran_per_day) 

# printing the sorted keys by their values using a for loop
print(f"\nOutputing the sorted value using a for loop (ascending order)")
for i in sorted_miles_ran_per_day:
    print(i[0], i[1])

# trying add more information to the sorted output.
# needed to convert the keys and values into a string to concatenate.
print(f"\nOutput with more information (ascending order)")
for i in sorted_miles_ran_per_day:
    print(f"On "+ str(i[0]) + " I ran " + str(i[1]) + " miles.")

# descending order sorting. use the reverse=True to sort in descending order.
d_sorted_miles_ran_per_day = sorted(miles_ran_per_day.items(), key=lambda x: x[1], reverse= True)
print(f"\nOutput with more information (descending order)")
for i in d_sorted_miles_ran_per_day:
    print(f"On "+ str(i[0]) + " I ran " + str(i[1]) + " miles.")

# check to see if a key already exist
# made a function for finding a key in the dictionary.
def find_keys():
    key_to_search = input("\nWhat key value would you like to search? ")
    key_to_search = key_to_search.title()
    if key_to_search in miles_ran_per_day:
        return (f"{key_to_search} is in the dictionary.")
    else:
        return (f"{key_to_search} is in the dictionary.")

print(find_keys())

# check to see if a value already exist
# made a function for finding a value in the dictionary.
def find_values():
    value_to_search = input("\nWhat key value would you like to search? ")
    value_to_search = value_to_search.title()
    if value_to_search in miles_ran_per_day:
        return (f"{value_to_search} is in the dictionary.")
    else:
        return (f"{value_to_search} is in the dictionary.")

print(find_values())

# alternate way to get value is to use the .get().
print("\nUsing .get() method to find data")
print("I ran " + str(miles_ran_per_day.get("Tuesday")) + " on Tuesday.")

# using for loops to iterate over a the dictionary:
print("\nUsing a for loop and items() method to print the dictionary")
for key, value in miles_ran_per_day.items():
    print(key, value)

# using for loops to print values greater than 5. use .values() method
print("\nUsing a for loop to print values greater than 5.")
for value in miles_ran_per_day.values():
    if value > 5:
        print(value)

# print both key and value if value is greater than 5. use .items() method.
print("\nUsing a for loop to print key and values for value greater than 5.")
for key, value in miles_ran_per_day.items():
    if value > 5:
        print(key, value)

# Creating a list of dictionary
miles_ran_per_day = [{
    'Day': 'Monday',
    'Miles': 15,
    'Heart-Rate': 'Super-Fast',
    'Overall Feeling': 'Great'
},
{
    'Day': 'Tuesday',
    'Miles': 12,
    'Heart-Rate': 'Fast',
    'Overall Feeling': 'Good'
},
{
    'Day': 'Wednesday',
    'Miles': 50,
    'Heart-Rate': 'Crazy-Fast',
    'Overall Feeling': 'Dead'
}]

# finding the minimun, maximum, total and average for the miles key of each dictionary.
# I had trouble with this. I was trying to loop over the and append the values for miles
# into a list, but I could get it to work. The solution below was found on:
# https://stackoverflow.com/questions/5320871/in-list-of-dicts-find-min-value-of-a-common-dict-field
# it appears to be a for loop in one and we can use the built functions of min, max, sum and mean.

mininum = min(item['Miles'] for item in miles_ran_per_day)
print(f"\nPrinting the lowest number of miles ran the list of dictionary:")
print(mininum)

maximum = max(d['Miles'] for d in miles_ran_per_day)
print(f"\nPrinting the highes number of miles ran in the list of dictionary:")
print(maximum)

total = sum(d['Miles'] for d in miles_ran_per_day)
print(f"\nPrinting the total number of miles from the list of dictionary:")
print(total)

# imported the statistics module to use the mean() function.
average = statistics.mean(d['Miles'] for d in miles_ran_per_day)
print(f"\nPrinting the average number of miles ran from list of dictionary:")
print(average)
