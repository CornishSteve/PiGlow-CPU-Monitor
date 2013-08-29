#!/usr/bin/python

from piglow import PiGlow
from time import sleep
import psutil

piglow = PiGlow()

# start at white
colour = 1

while True:
    # returns a value from 0 - 1 representing current CPU load
    cpu = psutil.cpu_percent()

    # now we need to scale that CPU level to the range 0 - 255 for PiGlow brightness
    brightness = max( (int)(cpu * 255), 1)

    # pick a speed that gets faster as the CPU usage increases
    speed = max ( 1.2 - cpu, 0.1 )

    # turn everything off, let's get ready to rumble
    piglow.all(0)

    # turn on the next "ring" of colour
    piglow.colour(colour, brightness)

    # sleep for a bit, i'm weary...
    sleep(speed)

    # increment to the next colour (reset to white if we're already on red)
    colour = colour + 1 if colour < 6 else 1
