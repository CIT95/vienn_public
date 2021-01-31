# Demonstrating fileNotFoundError exception
filename = 'test_scores.txt'

try: # Try to open this file
    f = open(filename) 
except FileNotFoundError: # If the file does not exist, do this:
    print("File is missing.")
else: # If the file exist, do this:
    print("File exist.")

# I also looked up how to print the contents of the text file, but that might have been
# more than this assignment asked..

# try: # Try to open this file
#     with open(filename) as f_object: #needs to be an object to use more options
#         contents = f_object.read() # reading the contents of the file
# except FileNotFoundError:
#     print(f"{test_scores} file is missing.") # if the file is not there.
# else:
#     print("The test scores are as follows:") #prin the test scores.
#     print(contents)