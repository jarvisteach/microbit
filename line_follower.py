from microbit import *


# function to detect if we're over a black line
def overLine(pin=pin0):
    # discard first reading
    pin.read_digital()
    sleep(5)
    # pin is high when reflecting
    # pin is low when over black & not reflecting
    return not pin.read_digital()


# function to determine direction to turn
def monitor(left=pin0, right=pin1):
    left = overLine(left)
    right = overLine(right)

    if not left:
        print("turn right")
    if not right:
        print("turn left")


while True:
    if not overLine():
        print("go back")
    else:
        print("over line")

    sleep(250)
