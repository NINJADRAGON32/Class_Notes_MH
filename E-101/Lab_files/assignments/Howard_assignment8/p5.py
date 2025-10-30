from sense_hat import SenseHat
from time import sleep, time
import random

sense = SenseHat()
sense.clear()

while True:
    sense.show_message("Get Ready!", text_colour=(255,255,255))
    sense.clear()
    wait_time = random.randint(1, 5)
    sleep(wait_time)

    sense.clear(0, 255, 0)
    start_time = time()


    pressed = False
    while not pressed:
        for event in sense.stick.get_events():
            if event.action == "pressed":
                end_time = time()
                reaction = end_time - start_time
                sense.clear()
                sense.show_message(f"{reaction:.2f}s", text_colour=(0,0,255))
                pressed = True

    # Short delay before next round
    sleep(4)
    sense.clear()
