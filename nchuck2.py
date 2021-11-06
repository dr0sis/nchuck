#Coffee shop exercise.

#Let's build a robot barista.

#Variables - A method of storing data for reuse

print("Hello, welcome to NetworkChuckCoffee!!!!!!!!!")

name = raw_input("What is your name? \n")
Menu = {1: "Espresso", 2: "Latte macchiato", 3: "American", 4: "Filtered"}

print("Hello " + name + ", thank you so much for coming in today. ")

question = raw_input("Would you like to see the menu? \n").lower()
if question == ("yes"):
    print(Menu[1] + "\n" + Menu[2] + "\n" + Menu[3] + "\n" + Menu[4] + "\n")
else:
    print("Please enter yes or no.")

choice = raw_input("What would you like? \n").lower()
if choice == "espresso":
    print("Thank you " + name + ", your " + Menu[1] + " will be ready soon")
elif choice == "latte macchiato":
    print("Thank you " + name + ", your " + Menu[2] + " will be ready soon")
elif choice == "american":
    print("Thank you " + name + ", your " + Menu[3] + " will be ready soon")
elif choice == "filtered":
    print("Thank you " + name + ", your " + Menu[4] + " will be ready soon")
else:
    print("Well screw you then, get bent")