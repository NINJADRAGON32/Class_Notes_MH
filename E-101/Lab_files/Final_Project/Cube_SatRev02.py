# Revision 1 of the Cube sat programing for the raspberry pi.
# these are the basic functions of the raspberry pi that will later allow the pi to be a crucial part of the game 

# Imports and Globals
import random as r
from sense_hat import SenseHat
sense = SenseHat
# ________________________________________________________________________________________
players = []
difficulty_colors=["red","orange","green","yellow"]
ui = "" 
gamestate = 0
index = 0
#-----------------------------------------------------------------------------------------
# Functions
def roll_dice():
    # rolls the dice
    return r.randint(1,8)

def assign_color():
    # assigns a color for the difficulty of the question
    return difficulty_colors[r.randint(0,len(difficulty_colors)-1)] 

def assign_turn_order(players):
    # when given a list of players will randomize the turn order.
    turn_Order = []
    while len(players) != 0:
        j = r.randint(0,(len(players))-1)
        turn_Order.append(players[j])
        players.pop(j)
    return (turn_Order)

def grabbing_players(ui):
    # asks the user for the list  of all the players
    """
        WARNING: will likely be modified or changed entirely for raspberry pi
    """
    sense.show_message("How many players!!", scroll_speed = 0.05,text_colour = [139,0,0], back_colour = [0,0,0])
    players = [
        '1': 
    ]
    ui = str(input("Please input player names and when you are done type q: "))
    while ui != "q": 
        players.append(ui)
        ui = str(input("Please input player names and when you are done type q: "))

# main ---------------------------------------------------------------------------------

grabbing_players(ui)
t_o = assign_turn_order(players)
print(f"Here is our turn order: {t_o}")
print(f"Starting game!!!!")
gamestate=1
while gamestate==1:
    print(f"it's {t_o[index]}'s turn")
    ui = str(input("press (r) to roll the dice and get your card color. "))
    roll = roll_dice()
    print(f"you rolled a {roll} and your card color is {assign_color()}")
    ui = str(input("Did you get the question right?(y/n): "))
    if ui =="y":
        print(f"AWESOME move forward {roll} spaces")
    else: 
        print("you suck haha loserrrr!!!!!!!!!!!")
    if index == (len(t_o)-1):
        index = 0
    else:
        index = index+1
    ui = str(input("did you win?(y/n): "))
    if ui == "y":
        gamestate=0


