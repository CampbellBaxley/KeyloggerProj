# Python Keylogger

This repository contains a Python-based keylogger designed for educational purposes and learning about system monitoring and logging techniques. I followed tutorials from the websites listed below to create the keylogger, then added my own implementation to email the "keylog.txt" file to the desired email address.  **This tool must be used responsibly and only with explicit permission from the owner of the device. Unauthorized use is illegal and unethical.**

## Features

- Logs all typed keys into a file "keylog.txt".
- Sends an email containing the keystroke logs when the escape key is pressed.
- The email is sent to a specified recipient via Gmail's SMTP server.

## Configuration
- sender_email: Your Gmail address
- sender_password: Your Gmail password or app-specified password
- recipient_email: The recipient's email address for sending the logs

## Running
- python keylogger.py

## Refrences

- GeeksForGeeks
    - https://www.geeksforgeeks.org/open-and-run-python-files-in-the-terminal/
- AskPython
    - https://www.askpython.com/python/examples/python-keylogger