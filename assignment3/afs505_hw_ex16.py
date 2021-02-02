#importing the fucntion argv from the sys module
from sys import argv

script, filename = argv

#printing warning before truncation
print(f"We're going to erase {filename}.")
print("If you don;t want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

#opening file
print("Opening the file...")
target = open(filename, 'w')

#truncating file
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

#writing to new file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#another way of writing to filename
target.write(f"""
{line1}.
{line2}.
{line3}.
""")


print("And finally, we close it.")
target.close() #close file
