#!/usr/bin/python
import time
from sense_hat import SenseHat

sense = SenseHat()

# sense.low_light = True

flash_delay = 0.1

sense.show_message(
    "Erica & Thomas",
    scroll_speed=0.025,
    text_colour=[0, 0, 255],
    back_colour=[255, 255, 0]
)

time.sleep(flash_delay)
sense.low_light = True
time.sleep(flash_delay)
sense.low_light = False
time.sleep(flash_delay)
sense.low_light = True
time.sleep(flash_delay)
sense.low_light = False
time.sleep(flash_delay)
sense.low_light = True
time.sleep(flash_delay)
sense.low_light = False
time.sleep(flash_delay)
sense.clear()

