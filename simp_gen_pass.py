#!/usr/bin/python
# Generate a random string of alpha-numeric and special characters in python
# Description: I *really* dislike using suggestion scripts from random plug-ins.
# Version: Python 3.12
# Author:  J4ck

import secrets
import string
import sys

# Creating library of characters
# Alpha:   abcdefghijklmnipqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# Numbers: 0123456789
# Special_Characters: !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~
alpha = string.ascii_letters
nums = string.digits
special_chars = string.punctuation
library = alpha + nums + special_chars

# Defaults
pass_length = 16 # default value if not overritten

if len(sys.argv) > 1:
    if '-l' in sys.argv:
        try:
            length_index = sys.argv.index('-l') + 1
            if length_index < len(sys.argv):
                pass_length = int(sys.argv[length_index])
                if 12 <= pass_length <= 128:
                    print(f"Default length overriden. Proceeding with new length: {pass_length}")
                else:
                    print("Length must be between 12 and 128. Ignoring and proceeding with 16 (default).")
                    pass_length = 16
        except (ValueError, IndexError):
            print("Invalid length value. Ignoring and proceeding with default.")
    else:
        print("Invalid flag provided. Proceeding with defaults.")
else:
    print("No flags provided. Proceeding with default settings.")
    
# Generate password
pwd = ''
for i in range(pass_length):
    pwd += ''.join(secrets.choice(library))
print("*** Password Generated ***")
print("**************************")
print(f"Password: {pwd}")
print(f"Password length: {pass_length}")
print("**************************")
