import json

file_name = './files/users.json'
# open and read users.json file
f = open(file_name)
#returns JSON object as a dictionary
data = json.load(f)
#closing file
f.close()

def add_user():
    new_username = input("Enter the new username (email): ")
    new_name = input(f"Enter the name of {new_username}: ")
    new_password = input(f"Enter the password for {new_username}: ")
    new_user = {
        'username': new_username,
        'name': new_name,
        'password': new_password
    }
    with open('./files/users.json', 'r+') as file:
        data = json.load(file)
        data['users'].append(new_user)
        file.seek(0)
        json.dump(data, file)
        
   
add_user()

