from sense_hat import SenseHat
sense = SenseHat()

# Colors
R = (150, 0, 0)
W = (255, 255, 255)
E = (0, 0, 0)

# IU trident picture (8x8)
picture = [
R,R,E,R,R,E,R,R,
R,R,E,R,R,E,R,R,
R,R,E,R,R,E,R,R,
R,R,R,R,R,R,R,R,
E,E,R,R,R,R,E,E,
E,E,E,R,R,E,E,E,
E,E,R,R,R,R,E,E,
E,E,E,E,E,E,E,E
]

sense.set_pixels(picture)

# Wait for joystick press
while True:
    for event in sense.stick.get_events():
        if event.action == "pressed" and event.direction == "middle":
            sense.show_message("GO IU!", text_colour=W, back_colour=R)
            sense.set_pixels(picture)
