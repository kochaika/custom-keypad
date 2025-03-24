import board
from digitalio import DigitalInOut, Direction, Pull
from pmk import PMK
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode


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
        # Return the inverted state of the switch (True when pressed, False when not pressed)
        return not self._switches[idx].value

    def i2c(self):
        return None


# Configure the LED pin (Pin 25 in this case)
led = DigitalInOut(board.GP25)  # Replace GP25 with your LED pin if needed
led.direction = Direction.OUTPUT

pins = [board.GP17, board.GP18]
pmk = PMK(SimpleGPIOHardware(pins))
pmk.keys[0].debounce = 0.005

keyboard = Keyboard(usb_hid.devices)
keycode = Keycode.ZERO


# Define key press handlers
@pmk.on_press(pmk.keys[0])
def handle_key0(key):
    led.value = True
    keyboard.send(Keycode.COMMAND, Keycode.SHIFT, Keycode.LEFT_BRACKET)


@pmk.on_release(pmk.keys[0])
def handle_key0_release(key):
    led.value = False


print("Press the keys connected to GP17 and GP18...")
while True:
    # Update the PMK instance to check for key presses
    pmk.update()

