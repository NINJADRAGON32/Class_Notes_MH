# Revision 1 of the Cube sat programing for the raspberry pi.
# these are the basic functions of the raspberry pi that will later allow the pi to be a crucial part of the game 

# Imports and Globals
import random as r
from sense_hat import SenseHat
sense = SenseHat
# ________________________________________________________________________________________
players = []
difficulty_colors=["R","O","G","Y"]
ui = "" 
gamestate = 0
index = 0
R = (150, 0, 0)
Y = (255,255,0)
G = (0,255,0)
O = (255,165,0)
W = (255, 255, 255)
E = (0, 0, 0)

one = [
E,E,E,E,E,E,E,E,
E,E,R,E,E,E,E,E,
E,E,R,E,E,E,E,E,
E,E,R,E,E,E,E,E,
E,E,E,E,E,E,E,E,
E,E,R,E,E,E,E,E,
E,E,R,E,E,E,E,E,
E,E,R,E,E,E,E,E
]
two = [
E,E,E,E,E,E,E,E,
E,E,R,R,R,R,E,E,
E,E,E,E,E,R,E,E,
E,E,E,E,E,R,E,E,
E,E,E,R,R,E,E,E,
E,E,R,E,E,E,E,E,
E,E,R,E,E,E,E,E,
E,E,R,R,R,R,E,E
]
three = [
E,E,E,E,E,E,E,E,
E,E,R,R,R,R,E,E,
E,E,E,E,E,R,E,E,
E,E,E,E,E,R,E,E,
E,E,E,R,R,E,E,E,
E,E,E,E,E,R,E,E,
E,E,E,E,E,R,E,E,
E,E,R,R,R,E,E,E
]
four = [
E,E,E,E,E,E,E,E,
E,E,R,E,E,R,E,E,
E,E,R,E,E,R,E,E,
E,E,R,E,E,R,E,E,
E,E,R,R,R,R,E,E,
E,E,E,E,E,R,E,E,
E,E,E,E,E,R,E,E,
E,E,E,E,E,R,E,E
]
five = [
E,E,E,E,E,E,E,E,
E,E,R,R,R,R,E,E,
E,E,R,E,E,E,E,E,
E,E,R,E,E,E,E,E,
E,E,R,R,R,R,E,E,
E,E,E,E,E,R,E,E,
E,E,E,E,E,R,E,E,
E,E,R,R,R,R,E,E
]
six = [
E,E,E,E,E,E,E,E,
E,E,R,R,R,R,E,E,
E,E,R,E,E,E,E,E,
E,E,R,E,E,E,E,E,
E,E,R,R,R,R,E,E,
E,E,R,E,E,R,E,E,
E,E,R,E,E,R,E,E,
E,E,R,R,R,R,E,E
]
seven = [
E,E,E,E,E,E,E,E,
E,E,R,R,R,R,E,E,
E,E,E,E,E,R,E,E,
E,E,E,E,E,R,E,E,
E,E,E,E,E,R,E,E,
E,E,E,E,E,R,E,E,
E,E,E,E,E,R,E,E,
E,E,E,E,E,R,E,E
]
eight = [
E,E,E,E,E,E,E,E,
E,E,R,R,R,R,E,E,
E,E,R,E,E,R,E,E,
E,E,R,E,E,R,E,E,
E,E,R,R,R,R,E,E,
E,E,R,E,E,R,E,E,
E,E,R,E,E,R,E,E,
E,E,R,R,R,R,E,E
]
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

def grabbing_players():
    # asks the user for the correct number of players up until 4
    num_players = 1
    sense.show_message("How many players!!", scroll_speed = 0.05,text_colour = [139,0,0], back_colour = [0,0,0])
    event = sense.stick.wait_for_event()
    while event.direction != 'middle' and event.action != 'pressed':
        if num_players==1:
            sense.set_pixels(one)
        elif num_players==2:
            sense.set_pixels(two)
        elif num_players==3:
            sense.set_pixels(three)
        elif num_players==4:
            sense.set_pixels(four)
        if event.direction == 'up':
            if num_players == 4:
                num_players=1
            else:
                num_players+=1
        elif event.direction =='down':
            if num_players == 1:
                num_players=4
            else: 
                num_players-=1

def turn():
    roll = roll_dice()
    color = assign_color()
    if roll==1:

        sense.set_pixels(one)
    elif roll==2:
        sense.set_pixels(two)
    elif roll==3:
        sense.set_pixels(three)
    elif roll==4:
        sense.set_pixels(four)



    return ()

# main ---------------------------------------------------------------------------------

grabbing_players()
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


