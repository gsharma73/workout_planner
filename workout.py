#Govind Sharma workout selector 

import random


Shoulders = ["Gada training", "Lateral Raises", "Bench Press", "Barbell Front Raise", "Front Press"]
Chest = ["Bench Press", "Landmine Shoulder Throw", "Barbell Front Raise", "Front Press", "Bench Dips"]
Bicep = ["Barbell Curl",]
Tricep = ["Bench Dip", "Gada training", "Bench Press" ,"Front Press"]
Forearms = ["Reverse Curl",]
Core  = ["Hip Thrusters", "Plank",]
Back = ["Gada Training", "Landmine Row", "Barbell Front Raise"]
Legs = ["Hip Thrusters", "Squats", ""]




print("\n\nWhich muscles would you like to work on today?"'\n')
print("Shoulder, Bicep, Tricep, Forearms")
print("Chest, Back, Core, Legs")
print("Enter end to stop")

userInput = "stretching"

while userInput != "end":
    userInput = input("-->")

    if userInput[:2].lower() == "sh":
        print(random.choice(Shoulders))

    elif userInput[:2].lower() == "tr":
        print(random.choice(Tricep))

    elif userInput[:2].lower() == "bi":
        print(random.choice(Bicep))

    elif userInput[:2].lower() == "fo":
        print(random.choice(Forearms))

    elif userInput[:2].lower() == "ch":
        print(random.choice(Chest))

    elif userInput[:2].lower() == "co":
        print(random.choice(Core))

    elif userInput[:2].lower() == "ba":
        print(random.choice(Back))

    elif userInput[:2].lower() == "le" or userInput[:2].lower() == "bu":
        print(random.choice(Legs))

    elif userInput[:1].lower() == "e":
        break

    else:
        #print("Error ~ Wrong input")
        break




