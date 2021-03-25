import json
file_name = './files/users.json'
# open and read users.json file
f = open(file_name)
#returns JSON object as a dictionary
data = json.load(f)
#closing file
f.close()
# helped from stack overflow regarding how to set a global variable.
glob_username = ''
glob_password = ''

def get_user_email():
    # getting the user's email address
    global glob_username
    glob_username = input("What is your user email? ")
    global glob_password
    glob_password = input("What is your password? ")
get_user_email()

def main_menu():
    print("\nPlease select from one of the following:")
    print('-' * 40)
    print("1 - Add a new user.")
    print("2 - Change password.")
    print("3 - View current users.")
    print("4 - Generate randomn password")
    user_choice = input()
    if user_choice == "1":
        add_user()

# def add_user():
#     new_username = input("Enter the new username (email): ")
#     new_name = input(f"Enter the name of {new_username}: ")
#     new_password = input(f"Enter the password for {new_username}: ")
#     new_user = {
#         'username': new_username,
#         'name': new_name,
#         'password': new_password
#     }
#     with open('./files/users.json', 'a') as user_dumped:
#         json.dump(new_user, user_dumped, indent = 4, sort_keys= True)


# validating user's email    
for user in data:
    if user['username'] == glob_username and user['password'] == glob_password:
        print("Access is Granted.")
        main_menu()
        break
    else:
        print('Invalid email.')
        get_user_email()

