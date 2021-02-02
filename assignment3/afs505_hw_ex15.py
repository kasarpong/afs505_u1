#importing the fucntion argv from the sys module
from sys import argv

#assigning variables to the argument variable
script, filename = argv

#opening text file
txt = open(filename)

#printing content of text file
print(f"Here's your file {filename}:")
print(txt.read())

#printing content of file by entering filename
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
