import os
from pyfiglet import Figlet
from termcolor import colored
VERSION = "1.0.0"
SOURCE = "https://github/xulpn/BrOwSeR"
def title():
    ascii_banner = Figlet(font='slant')
    print(colored("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", "green", attrs=["bold"]))
    print(colored(ascii_banner.renderText("BrOwSeR"), "green", attrs=["bold"]))
    print(colored(f"version: v{VERSION}", "green", attrs=["bold"]))
    print(colored(f"source: {SOURCE}", "green", attrs=["bold"]))
    print(colored("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", "green", attrs=["bold"]))

def start():
    print(colored(f"Selecting configuration file...", "yellow", attrs=["bold"]))

def note(text):
    print(colored("NOTE:", "green", attrs=["bold"]), colored(text, "yellow", attrs=["bold"]))
