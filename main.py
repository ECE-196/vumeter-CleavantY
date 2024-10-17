import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

tVar = 0
# Time variable:
# Keeps track of how many 1/10ths of a second have passed

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33, # type: ignore
    board.IO34, # type: ignore
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

# main loop
while True:
    volume = microphone.value

    # "volume // 4861.5" corresponds the volume reading to each LED
    # ie: "volume = 48615" means "if(i <= volume//4861.5)" executes for each i in the range, therefore turning on each LED

    for i in range(0,11):
        if (i <= volume//4861.5):
            leds[i].value = 1

    # byron sucks 

    for i in reversed(range(0,11)):
        if (leds[i].value == 1 and tVar == 0):
            leds[i].value = 0
            break
        
    print(volume)
    sleep(.1)
    tVar += 1
    tVar = tVar % 5

    # 48615



