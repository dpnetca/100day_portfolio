#!/usr/bin/env python
"""
Morse Code Converter
Author: Denis Pointer (https://www.dpnet.ca)

Simple CLI portfoltio project to convert between text to Morse Code
"""

import os
import re
import sys

from art import logo
from codes import itu_code
from menu import Menu


def clear_screen():
    """issue clear screen command, "clear" for linux/mac "cls" for windows"""
    os.system("cls" if os.name == "nt" else "clear")


def text_to_morse():
    """
    Prompt user for String, convert it to Morse Code and display
    """
    clear_text = input("\nPlease Enter String to Decode: ")

    morse_text = [itu_code[x] for x in clear_text.upper()]

    # Append "End of Message" code
    morse_text.append("  .-.-.")
    print("Morse Code:")
    print(" ".join(morse_text))
    input("\n\n press enter to continue")


def morse_to_text():
    """
    Prompt user for Morse Code, convert it to a string and display
    """

    reverse_itu_code = {v: k for k, v in itu_code.items()}

    morse_text = input("\nPlease Enter Morse Code to Decode: ")

    # Assume 2 or more spaces is break in word, use ' _ ' to reflect this
    morse_text = re.sub(r"\s\s+", " _ ", morse_text)
    reverse_itu_code["_"] = " "

    morse_list = morse_text.split(" ")

    # if last element is the End of Message element, remove it
    if morse_list[-1] == ".-.-.":
        morse_list = morse_list[:-2]

    clear_text = [reverse_itu_code[x] for x in morse_list]

    print("Clear text message:")
    print("".join(clear_text))
    input("\n\n press enter to continue")


def main():
    clear_screen()
    print(logo)
    print("Welcome to 100 Days of Code Morse Code Converter by dpnet.ca\n")

    menu = Menu()
    menu.add_option("1", "Convert text to Morse Code")
    menu.add_option("2", "Convert Morse Code to Text")
    menu.add_option("q", "Quit")

    end = False
    while not end:
        # selection = menu()
        selection = menu.display_menu()
        if selection == "1":
            text_to_morse()
        elif selection == "2":
            morse_to_text()
        elif selection == "q":
            sys.exit(0)
        else:
            print("Unexpected Error, please contact author")
            sys.exit(1)
        clear_screen()
        print(logo)


if __name__ == "__main__":
    main()
