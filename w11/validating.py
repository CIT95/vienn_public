import json

file_name = './files/users.json'
# open and read users.json file
f = open(file_name)
#returns JSON object as a dictionary
data = json.load(f)
#closing file
f.close()
print(type(data))
glob_username = ''
glob_password = ''

def get_user_email():
    # getting the user's email address
    global glob_username
    glob_username = input("What is your user email? ")
    global glob_password
    glob_password = input("What is your password? ")


def validate_user():
    for user in data['users']:
        if user['username'] == glob_username and user['password'] == glob_password:
            print(f"Hello {glob_username}!")
            main_menu()
            break
        else:
            print("Invalid Credentials")
   
get_user_email()
validate_user()