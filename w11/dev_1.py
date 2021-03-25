import random # To use the random.sample()
import json
# run = 'y' # To loop the program
# while run == 'y':  # Loop to run the program again if desired.
		
# " This program verifies and greet users. The user 'admin' has the ability to add users to the list."
# valid_users = ['Bob', 'Johnny', 'Jax', 'Kitana'] # List of valid users.

# open and read users.json file
f = open('./files/users.json')
#returns JSON object as a dictionary
data = json.load(f)
#closing file
f.close()

# getting the username from the user:
user_name = input("What is your user email? ")

# # Iterating through the json list
# for user in data['users']:
# 	print(user)

# for user in data.items():
# 	print(user)

# for key, value in data.items():
# 	print(key, value)

# stack overflow helped with this. I had trouble understanding where to 
# put the username key in. It's an object so we would want to iterate on it:
for user in data['users']:
	if user['username'] == user_name:
		print("hello")

# def add_user():
# 	""" Let's the user add more users to the list"""
# 	print(f"\nWould you like to add a new users? (y or n)")
# 	add_user = input()
# 	if add_user.lower() == 'y':
# 		new_user = input(f"\nWhat is the name of the new user? ")
# 		if new_user in valid_users:
# 			print(f"{new_user} is already on the list of valid users.")
# 		else:
# 			valid_users.append(new_user)
# 			print("Adding new user......\n")
# 	else:
# 		print("Undertsood. No new user will be added.")

# def verify_greet_user(user_name):
# 	""" Verify the user and returns the appropriate message."""
# 	if user_name == "admin":
# 			raise Exception
# 	elif user_name in valid_users:
# 		return (f"\nWelcome {user_name.title()}, it's great to see you again.")
# 	elif user_name == '':
# 		return ('Please enter a username. The username cannot be blank.')
# 	else:
# 		return (f"User is not found.")

# def current_user():
# 	""" Displays to the list of current users. """
# 	print(f"\nThe following is a list of valid users:")
# 	for user in valid_users:
# 		print(user.title())
# 	print("\nIf you find this to be an error, please contact your local administrator.")

# def new_user_list():
# 	""" Displays the new list of users. """
# 	print(f"\nThis is the most current list of valid users: ")
# 	for user in valid_users:
# 		print(user.title())

# def welcome_msg():
# 	""" Print the appropriate welcome message."""
# 	print(verify_greet_user(user_name))

# def rand_passwd_gen():
# 	""" Function to create a random password from two inputs. """
# 	print(f"\nWould you like to create a random password? (y or n): ")
# 	pass_continue = input()
# 	if pass_continue.lower() == 'y':
# 		string1 = str(input("Enter a value to use: "))
# 		string2 = str(input("Enter a second value to use: "))

# 		newstring = list(string1) + list(string2)
# 		shuff_string = ''.join(random.sample(newstring, len(newstring))) 
# 		#learned of the .join() method from note.nknk.me. Initially, was going to use a loop.
# 		print(f"\nThis is the password generated from your inputs: \n{shuff_string}. \nKeep it in safe place.")

# 		def pass_secure(shuff_string):
# 			if len(shuff_string) < 16:
# 				return f"For a more secure password, consider increasing the number of characters to 16."
# 			if len(shuff_string) > 16:
# 				return f"Definitely secure, but might be hard to remember."
# 		print(pass_secure(shuff_string))
# 	elif pass_continue == 'n':
# 		print("Maybe another time.")
		
# 	else:
# 		print("Not a valid input.")

# # Retrieving the username from user.	
# print("Please enter your username: ") 
# user_name = input()

# # this block will execute for all users except 'admin'
# try: 
# 	verify_greet_user(user_name)
# 	welcome_msg()
# 	# Adding this bit to ensure a username is entered. No username no access.
# 	if user_name == '' or user_name not in valid_users:
# 		print("ACCESS DENIED.") 
# 	else:
# 		current_user()
# 		rand_passwd_gen()

# # This block of coding only runs for the 'admin'. The add_user() is only available to the admin.
# except Exception: 
# 	print('Please enter your password: ')
# 	admin_pass = input()
# 	if admin_pass == 'admin':
# 		print("\nWelcome Admin")
# 		add_user()
# 		new_user_list()
# 		rand_passwd_gen()
# 	else: 
# 		print(f"Incorrect Password. ACCESS DENIED.")

# Loop to continue running program from week 2 Code Along.
	# print(f'\nWould you like to login as a different user? (Y for yes): ') 
	# run = input()
	# run = run.lower()
	# if run != 'y':
	# 	print('Signing off...')
	# continue

#more comments
#concise function
#initaliation function
#while loop to function.