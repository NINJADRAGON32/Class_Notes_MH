from sense_hat import SenseHat
sense = SenseHat()

colors = {
    'up': (255, 0, 0),      # Red
    'right': (0, 255, 0),   # Green
    'left': (255, 255, 0),  # Yellow
    'down': (0, 0, 255),    # Blue
    'middle': (255, 255, 255) # White
}

dark = (0, 0, 0)

while True:
    event = sense.stick.wait_for_event()
    if event.action == 'pressed':
        if event.direction in colors:
            sense.clear(colors[event.direction])
    elif event.action == 'released':
        sense.clear(dark)
