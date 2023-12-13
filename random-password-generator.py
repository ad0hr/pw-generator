from lib2to3.pgen2.pgen import generate_grammar
"""
generates random password 10 characters long with one special character and two digits

then stores each password and username in random-pw.txt
"""
import string
import secrets


alphabet = string.ascii_letters
digits = string.digits
special = string.punctuation

all_characters = alphabet + digits + special

site = input("Enter the site for which the username and password is for: ")
username = input("Enter username: ")

special_count = 0
digit_count = 0

while True:
    generated_password = ''
    for i in range(10):
        new_letter = secrets.choice(all_characters)
        generated_password = generated_password + new_letter
    if (any(char in special for char in generated_password) and sum(char in digits for char in generated_password)>=2):
        break 
    
# print(generated_password)

my_file = open("random-pw.txt", "a")
new_password = generated_password
my_file.write("Site: " + site)
my_file.write("\n")
my_file.write("Username: " + username)
my_file.write("\n")
my_file.write("Password: " + new_password)
my_file.write("\n")
my_file.write("\n")
my_file.close()

print("Randomly generated password to use: " + generated_password)
print("Password and username has been stored in file")