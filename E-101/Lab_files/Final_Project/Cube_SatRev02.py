# Revision 2 of the Cube sat programing for the raspberry pi.
# these are the basic functions of the raspberry pi that will later allow the pi to be a crucial part of the game 

# Imports and Globals
import random as r
from sense_hat import SenseHat
sense = SenseHat()
from time import sleep
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
    while not (event.direction == 'middle' and event.action == 'pressed'):
        sleep(1)
        if num_players == 1:
            sense.set_pixels(one)
        elif num_players == 2:
            sense.set_pixels(two)
        elif num_players == 3:
            sense.set_pixels(three)
        elif num_players == 4:
            sense.set_pixels(four)

        event = sense.stick.wait_for_event()  
        if event.direction == 'up':
            num_players = 1 if num_players == 4 else num_players + 1
        elif event.direction == 'down':
            num_players = 4 if num_players == 1 else num_players - 1
    return (num_players)

def take_turn(p):
    # this funtion programs the turn order per player
    event = sense.stick.wait_for_event()
    while not (event.direction == 'middle' and event.action == 'pressed'):
        sense.show_message(f"Player {p}'s turn  ", scroll_speed = 0.05,text_colour = [139,0,0], back_colour = [0,0,0])
    roll = roll_dice()
    C = assign_color()
    sense.clear()
    sense.set_pixels([
    C,C,C,C,C,C,C,C,
    C,C,C,C,C,C,C,C,
    C,C,C,C,C,C,C,C,
    C,C,C,C,C,C,C,C,
    C,C,C,C,C,C,C,C,
    C,C,C,C,C,C,C,C,
    C,C,C,C,C,C,C,C,
    C,C,C,C,C,C,C,C
    ])
    sleep(4)
    sense.clear()
    if roll==1:
        sense.set_pixels(one)
    elif roll==2:
        sense.set_pixels(two)
    elif roll==3:
        sense.set_pixels(three)
    elif roll==4:
        sense.set_pixels(four)
    elif roll==5:
        sense.set_pixels(five)
    elif roll==6:
        sense.set_pixels(six)
    elif roll==7:
        sense.set_pixels(seven)
    elif roll==8:
        sense.set_pixels(eight)
    event = sense.stick.wait_for_event()
    while not (event.direction == 'middle' and event.action == 'pressed'):
        sense.show_message("click to end your turn!!", scroll_speed = 0.05,text_colour = [139,0,0], back_colour = [0,0,0])
    return

# main ---------------------------------------------------------------------------------
grabbing_players()
sense.show_message("Starting Game", scroll_speed = 0.05,text_colour = [139,0,0], back_colour = [0,0,0])
gamestate=1
p = 1
turn = 0
while gamestate == 1:
    take_turn(p)
    if turn>=5:
        sense.show_message("Did u win? up-yes down-no", scroll_speed = 0.05,text_colour = [139,0,0], back_colour = [0,0,0])
        event = sense.stick.wait_for_event()
        if event.direction == 'up': 
            gamestate = 0
            sense.show_message(f"Congratulations, player {p} wins!!!!!", scroll_speed = 0.05,text_colour = [139,0,0], back_colour = [0,0,0])
            break
        elif event.direction =='down':
            gamestate =1
    if p==4:
        p=1
    else:
        p+=1
    turn +=1


            

    







