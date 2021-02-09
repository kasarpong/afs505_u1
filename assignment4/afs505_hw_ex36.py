from sys import exit

def best_sch():
    print("Let' see how smart you are")
def none():
    print("Wise up and choose Cougars")
best_sch()

print("Which school do you prefer? 'cougars', 'huskies' or 'none'")

sch_choice = input("> ")
if "cougars" in sch_choice:
    which_sch = str(sch_choice)
    print("You rock")
elif "huskies" in sch_choice:
    print("Boooo!!! You suck big time!!")
else:
    none()
