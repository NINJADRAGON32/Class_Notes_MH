from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()

dice_faces = {
    1: [(3,3)],
    2: [(1,1),(5,5)],
    3: [(1,1),(3,3),(5,5)],
    4: [(1,1),(1,5),(5,1),(5,5)],
    5: [(1,1),(1,5),(3,3),(5,1),(5,5)],
    6: [(1,1),(1,5),(3,1),(3,5),(5,1),(5,5)]
}

def show_dice(num):
    sense.clear()
    for x, y in dice_faces[num]:
        sense.set_pixel(x, y, 255, 255, 255)

while True:
    x, y, z = sense.get_accelerometer_raw().values()
    if abs(x) > 1.5 or abs(y) > 1.5 or abs(z) > 1.5:
        n = random.randint(1, 6)
        show_dice(n)
        sleep(2)  