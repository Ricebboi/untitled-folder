name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "Left".lower(): 
    answer = input("You come to a river, you can walk around it or swim across. Type walk to walk around and swim to swim across. ").lower()

    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")

if answer == "Right".lower():
    answer = input("You come to a forest. Do you take the rocky path to the mountain or the paved path to the town? Type mountain for rocky path and town for paved path ")

    if answer == "mountain":
        print("You encounter a dragon and fight it for hours. You die because you tripped over a branch and fire came down and melted you.")
    elif answer == "town":
        print("You arrived at a town called Nosgoth. The people are friendly and offer you food and water for your journey. Congrats you survived! ")
    else:
        print("Not a valid option. You lose. ")
