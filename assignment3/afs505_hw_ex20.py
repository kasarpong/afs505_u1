#importing the fucntion argv from the sys module
from sys import argv

script, input_file = argv

#defining function to read file
def print_all(f):
    print(f.read())

#defining function to set file position to beginning
def rewind(f):
    f.seek(0)
#function function to count number of lines in text file
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

#printing while leaving a line between
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
