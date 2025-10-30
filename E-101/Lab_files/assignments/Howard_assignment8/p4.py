from sense_hat import SenseHat
import random
from time import sleep

sense = SenseHat()

while True:
    number = random.randint(1, 4)
    sense.show_message("Guess!", text_colour=(255,255,255))
    
    event = sense.stick.wait_for_event()
    if event.action == 'pressed':
        guess = {'up':1, 'right':2, 'left':3, 'down':4}.get(event.direction, 0)
        if guess == number:
            sense.show_message("Correct!", text_colour=(0,255,0))
        else:
            sense.show_message(f"Wrong! It was {number}", text_colour=(255,0,0))
        sleep(1)
