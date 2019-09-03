#! /usr/bin/python3
# Launches a map in the browser using an address from the command lne or clipboard

import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()

webbrowser.open('http://www.google.com/maps/place/' + address)