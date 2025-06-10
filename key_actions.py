from adafruit_hid.keycode import Keycode

# Use Keycodes from here: https://github.com/adafruit/Adafruit_CircuitPython_HID/blob/main/adafruit_hid/keycode.py

key_actions = {
    0:  [],
    1:  [Keycode.LEFT_ARROW],
    2:  [Keycode.DOWN_ARROW],
    3:  [Keycode.RIGHT_ARROW],
    4:  [Keycode.SPACEBAR],
    5:  [Keycode.OPTION],
    6:  [Keycode.COMMAND],
    7:  [Keycode.UP_ARROW],
    8:  [Keycode.A],
    9:  [Keycode.T],
    10: [Keycode.B],
    11: [Keycode.COMMAND, Keycode.SHIFT,Keycode.A],
    12: [Keycode.COMMAND, Keycode.SHIFT,Keycode.I],
    13: [Keycode.BACKSPACE],
    14: [Keycode.LEFT_SHIFT],
    15: [Keycode.COMMAND, Keycode.SHIFT, Keycode.LEFT_BRACKET],
    16: [Keycode.COMMAND, Keycode.B],
    17: [Keycode.COMMAND, Keycode.SHIFT, Keycode.RIGHT_BRACKET],
    18: [Keycode.COMMAND, Keycode.SHIFT,Keycode.M],
    19: [Keycode.COMMAND, Keycode.SHIFT,Keycode.E],
    20: [],
    21: [Keycode.I],
    22: [Keycode.OPTION, Keycode.X],
    23: [Keycode.O],
    24: [Keycode.COMMAND, Keycode.Z],
    25: [Keycode.COMMAND, Keycode.SHIFT, Keycode.Z],
}
