import board
from digitalio import DigitalInOut, Direction, Pull
from pmk import PMK
import usb_hid
from adafruit_hid.keyboard import Keyboard

from key_actions import key_actions


class DummyDisplay:
    def set_pixel(self, idx, r, g, b):
        pass


class SimpleGPIOHardware:
    def __init__(self, pins):
        self._switches = [DigitalInOut(pin) for pin in pins]

        for switch in self._switches:
            switch.direction = Direction.INPUT
            switch.pull = Pull.UP

        self._display = DummyDisplay()
        self._i2c = None

    def set_pixel(self, idx, r, g, b):
        self._display.set_pixel(idx, r, g, b)

    def num_keys(self):
        return len(self._switches)

    def switch_state(self, idx):
        # Return the inverted state of the switch because of Pull.UP
        # True when pressed, False when not pressed
        return not self._switches[idx].value

    def i2c(self):
        return None


# Configure the built-in LED pin
led = DigitalInOut(board.GP25)
led.direction = Direction.OUTPUT

pins = [
    board.GP0, board.GP1, board.GP2, board.GP3, board.GP4,
    board.GP5, board.GP6, board.GP7, board.GP8, board.GP9,
    board.GP10, board.GP11, board.GP12, board.GP13, board.GP14,
    board.GP15, board.GP16, board.GP17, board.GP18, board.GP19,
    board.GP20, board.GP21, board.GP22, board.GP26, board.GP27, board.GP28
]

pmk = PMK(SimpleGPIOHardware(pins))

for key in pmk.keys:
    key.debounce = 0.005

keyboard = Keyboard(usb_hid.devices)


def on_key_press(index):
    print("\tPress: " + str(index))
    led.value = True
    action = key_actions.get(index, [])  # default to empty action
    if action:
        print("\tAction: " + str([hex(x) for x in action]))
        keyboard.press(*action)


def on_key_release(index):
    print("Release: " + str(index))
    led.value = False
    action = key_actions.get(index, [])  # default to empty action
    if action:
        print("Action: " + str([hex(x) for x in action]))
        keyboard.release(*action)


# Dynamically register handlers for each button
for i, key in enumerate(pmk.keys):
    @pmk.on_press(key)
    def handle_press(k, idx=i):
        on_key_press(idx)


    @pmk.on_release(key)
    def handle_release(k, idx=i):
        on_key_release(idx)

print("Ready!")
while True:
    # Update the PMK instance to check for key presses
    pmk.update()
