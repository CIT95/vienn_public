valid_users = ['bob', 'johnny', 'jax', 'kitana']

print("Please enter your username: ")
user_name = input()

if user_name in valid_users:
	print(f"\nWelcome {user_name.title()}, it's great to see you again.")
else:
	print("ACCESS DENIED.")
	exit()

print(f"\nThe following persons are valid users:")
for user in valid_users:
	print(user.title())

print(f"\nWould you like to add a new users? (y or n)")
add_user = input()
if add_user == 'y':
	new_user = input(f"\nWhat is the name of the new user? ")
	valid_users.append(new_user)
	print("Adding new user......\n")
else:
	print("Undertsood. No new user will be added.")
	exit()

print(f"\nThis is the most current list of valid users: ")
for user in valid_users:
	print(user.title())