#Game Idea - you are walking through a forest and come across a bridge being guarded by a troll, you can either try to pass the troll or go around the bridge. When passing the troll he will flip a coin. if you go around you can find a rotting log that might break when you cross
#coin flip on bridge
#
#Modules
import math
import random

#Game Start function
directions = ["Left","Right","Back","Forward"]
def Start():
    print("You awake on a path in a forest, you look around to see your surroundings.")
    print("Looking around you can see there is a bridge to your LEFT. \nTo your RIGHT, there is what seems to be an abandoned mine.")
    print("Which way do you want to go? \n LEFT \n RIGHT")
    Decision_One()
def Decision_One():
    choice = input()
    #choice right
    if choice.upper() == "RIGHT":
        print("You walk up to the abandoned mine and see a sign that says \"Danger Keep Out\" \n would you like to \n[1]Enter the Mine \n[2]Take the path to the bridge")
    elif choice.upper() == "LEFT":
        print("Walking along the path you come to a bridge. \n Looking around you can see a tall and imposing troll standing on the bridge continully flipping a flipping a large disc to him self. \n To the left you can see")
#random chance generator
def chance(range):
    return random.randrange(range)

#
print("Walking along the path you come to a bridge. \n Looking around you can see a tall and imposing troll standing on the bridge continully flipping a flipping a large disc to him self. \n To the left you can see")

# Start()