"""
Exercise 6-a:Exercise 6-a: Calling Elements of a Python List (Index 0)
Assign the first element of the list to answer_1 on line 4
"""
lst=[11, 100, 99, 1000, 999]
answer_1 = lst[0]

print(answer_1)
# I was able to complete this without any hint, solution or google assistance.

"""
Exercise 6-b: Calling List Elements and Indexing
And let's print the second element directly inside print function.
This time print the second element of the list directly on line 17. You should get 100.
"""
lst=[11, 100, 101, 999, 1001]

print(lst[1])
# I was able to complete this without any hint, solution or google assistance.

""" Exercise 6-c: Calling List Elements (Negative Index)
And the last element.
Print the last element of the list through variable answer_1.
"""
lst=[11, 100, 101, 999, 1001]
#Type your answer here.

answer_1= lst[-1]

print(answer_1)

"""
Exercise 6-d: Append method to add items to the end of Python Lists
.append method will let you add items to your lists.
On line 39, add the string "pajamas" to the list with .append() method
"""
gift_list=['socks', '4K drone', 'wine', 'jam']
# Type your code here.
gift_list.append('pajamas')


print(gift_list)
# I was able to complete this without any hint, solution or google assistance.

"""
Exercise 6-e: List inside List (Python Nested Data)
Lists can hold many type of data inside them. You can even add another list to a list as its element. This is called nested data in Python.
#On line 53, this time add the sub-list: ["socks", "tshirt", "pajamas"] to the end of the gift_list.
"""
gift_list=['socks', '4K drone', 'wine', 'jam']
# Type your code here.
gift_list.append(["socks", "tshirt", "pajamas"])


print(gift_list)
# I was able to complete this without any hint, solution or google assistance.

"""
Exercise 6-f: Insert method to add to a specified index of a Python List
.insert() lets you specify the index you want to add your item.
On line 67, this time insert "slippers" to index 3 of gift_list.
"""
gift_list=['socks', '4K drone', 'wine', 'jam']
# Type your code here.
gift_list.insert(2, 'slippers')


print(gift_list)
# I got it wrong the first time. I assume index 3 meant [3] but it really meant to do [2].

"""
Exercise 6-g: Index method to get the index of a List Item
With .index() method you can learn the index number of an item inside your list. 
Assign the index no of 8679 to the variable answer_1.
"""
lst=[55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
#  Type your code here.

answer_1= lst.index(8679)

print(answer_1)
#I got the answer on the second try. The first try I made the mistake of putting '' around the number. The value is an integer and is not a string.

"""
Exercise 6-h: Adding a different type of element to a List using Append
Using .append() method, add a new list to the end of the list which contains strings: "Navigator" and "Suburban".
lst=["CRV", "Outback", "XC90", "GL", "Cherokee", "Escalade"]
"""
lst=["CRV", "Outback", "XC90", "GL", "Cherokee", "Escalade"]
#  Type your code here.
lst.append(["Navigator", "Suburban"])


print(lst)

# I was able to complete this without any hint, solution or google assistance.

"""
Exercise 6-i: Removing the last item of a list (.remove() method)
Using .remove() method, clear the last element of the list.
"""
lst=[55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
#  Type your code here.
lst.remove(99)


print(lst)
# I got this on the second try. I thought I could use lst.remove([-1]),
#  but it returned a ValueError. 
# Turns out the .remove() takes the actual value to be remove

"""
Exercise 6-j: Reversing a Python list (.reverse() method)
Using .reverse() method, reverse the list.
"""
lst=[55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
#  Type your code here.
lst.reverse()


print(lst)
# I was able to complete this without any hint, solution or google assistance.

"""
Exercise 6-k: Count Method to get the amount of an item in a list
Using .count() method, count how many times 6 occur in the list.
"""
lst=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
#  Type your code inside print() function.

answer_1= lst.count(6)

print(answer_1)
# I was able to complete this without any hint, solution or google assistance.

"""
Exercise 6-l: Adding up all the items in a List w/ Sum Function
What is the sum of all the numbers in the list?
"""
lst=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]

#  Type your code on line 4:
answer_1= sum(lst)

print(answer_1)
# I was able to complete this without any hint, solution or google assistance.

"""
Exercise 6-m: Max Function to Get the Lowest Value in a List
What is the minimum value in the list?
"""
lst=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]

#  Type your code on line 4:
answer_1= min(lst)

print(answer_1)
# I got this on the second try because I used max(lst) first because the exercise name was Max Function.

"""
Exercise 6-n: Max Function to Get the Highest Value in a List
What is the maximum value in the list?
"""
lst=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]

#  Type your code on line 4:
answer_1=max(lst)

print(answer_1)
# I was able to complete this without any hint, solution or google assistance.

"""
