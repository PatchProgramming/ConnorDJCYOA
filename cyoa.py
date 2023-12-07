#Game Idea - you are walking through a forest and come across a bridge being guarded by a troll, you can either try to pass the troll or go around the bridge. When passing the troll he will flip a coin. if you go around you can find a rotting log that might break when you cross
#coin flip on bridge
#
#Modules
import random
import time
#Game Start function
directions = ["Left","Right","Back","Forward"]
def Start(): #main function which calls all others
    print("You awake on a path in a forest, you look around to see your surroundings.")
    print("Looking around you can see there is a bridge to your LEFT. \nTo your RIGHT, there is what seems to be an abandoned mine.")
    print("Which way do you want to go? \n LEFT \n RIGHT")
    Decision_One()
def Decision_One():
    choice = input("Please enter LEFT or RIGHT: ")
    #choice right
    if choice.upper() == "RIGHT":
        mineDecision()
    elif choice.upper() == "LEFT":
        pathDecision()
    elif choice.upper() == "EXIT()":
        exit()
    else:
        print("Adventurer I didn't catch that... do you want to go LEFT or RIGHT?")
        Decision_One()
def mineDecision():
    #if else statement for options
    print("""\nYou walk up to the abandoned mine and see a sign that says \"Danger Keep Out\".
    would you like to: 
    [1]:Enter the Mine
    [2]:Take the path to the bridge""")
    time.sleep(2)   
    choice = input("Enter a number to make your choice:  ")
    if choice == "1":
        print("""
        
                            As you enter the mine, the walls shake and the entrance collapes and a boulder pins you to the floor.
                                    As the light from the entrance fades a sign clatters infront of you.
        Squinting and using your last bit of energy you can make out the words\"Danger Keep Out\" and you think to yourself that maybe you should have listened...
            GAME OVER""")
        exit()
    elif choice == "2":
        pathDecision()
    elif choice == "exit":
        exit()
    else:
        print("Adventurer I didn't catch that... Lets try again")
        mineDecision()

#funtion for logic of the Path decision
def pathDecision():
    print("\nWalking along the path you come to a bridge. \nLooking around you can see a tall and imposing troll standing on the bridge continully flipping a flipping a large disc to himself. \n To the left you can see what looks like an old rope swing.\nThere is a rushing River beneath both which you don't thing you can swim across")
    print("""Would you like to:
    [1]:cross the bridge and face the troll
    [2]:go the the left and inspect the rope swing
    [3]:try swimming across
    [4]:Go back to the mine""")
    time.sleep(5)
    choice = input("Enter a number to make your choice: ")
    #if else statement for options
#random chance generator
def chance(range):
    return random.randrange(range)

#game start
Start()