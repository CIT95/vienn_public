# Dev 1 attempt with OOP:

class Users():
    def __init__(self, name, password):
        self.name = name
    
    def main_menu(self):
        print(f"MAIN MENU for {self.name}")

class Admin(Users):
    def add_user(self):
        new_user = input(f"Welcome {self.name}, please enter the name of the new user: ")
        print(f"{new_user} has been added.")

class Regular(Users):
    def hello(self):
        print(f"{self.name} Your choice are limited because you a regular user.")

u1 = Users("Johnny", "12323")
u2 = Admin("Peter", "pumpkineater")
u3 = Regular("Jack", "pumpkin King")

u2.main_menu()
u2.add_user()

u1.main_menu()
u3.hello()

# Fun OOP Version
# Creating parent class:

class Matrix():
    """
    create a parent class for matrix characters
    """
    def __init__(self, name):
        self.name = name
    
    def hello(self):
        print(f"Welcome to the Matrix, {self.name}")

    def choice(self):
        choice = input("Will you take red pill or blue pill? ")
        if choice.lower() == "blue":
            print(f"Stay in the Matrix, {self.name}.")
        elif choice.lower() == "red":
            print(f"Time to unplug, {self.name}.")
        else:
            print("Not picking a pill is also a choice.")

# Creating child classes:

class TheOne(Matrix):
    """
    Child class is for the 'One'
    """
    def hello(self):
        print(f"Welcome {self.name}. You are the one.")

class Agent(Matrix):
    """
    Child class for agents in the Matrix
    """
    def hello(self):
        print(f"Agent {self.name}, it is inevitable.")

neo = TheOne("Neo")
smith = Agent("Smith")
vien = Matrix("Vien")

print("\nAll though each class is using the same method, each have a different output: \n")
neo.hello()
smith.hello()
vien.hello()

print("Both child class inherit the choice() method from their parent: ")
neo.choice()
smith.choice()

# test code:
# class Users():
#     def __init__(self, name, password):
#         self.name = name
#         self.password = password

#     def welcome(self):
#         print(f"Welcome {self.name}, it's good to see you again.")

#     def secret(self):
#         print("There is no secret")

# class SuperUser(Users):
#     def secret(self):
#         print("The secret password is ****.")


# user1 = Users("John", "12344")

# user1.welcome()
# user1.secret()

# su = SuperUser("King", "123433")
# su.secret()
