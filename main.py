#!/usr/bin/env python3
from modules import *
import sys
from pyfiglet import Figlet
from termcolor import colored
import os
import time


# @main
# Description:
#
#

def main():
    ascii_banner = Figlet(font='slant')
    print(ascii_banner.renderText("BrOwSeR"))
    gdata = data.get()
    main_br = None
    test_br = None
    temp_br = None
    run_main = False
    exit_p = False
    if [gdata["browser"] == "Firefox"]:

        if [gdata["test-page"] == "yes"]:
            tserver.start()
            test_br = browser.start_test_page(gdata)
            tserver.stop()
        print(colored("NOTE: ", "red", attrs=['blink', "bold"]), colored(" See the test page if the right configuration is set!\n", "yellow", attrs=["bold"]))
        con = input("continue (y/n): ")
        if con != 'y':
            print("Exiting...")
            exit()
        else:
            main_br = browser.start_firefox(gdata)

    # for files in os.listdir(path):
    #     file = os.path.join(path, files)
    #     print(file)

main()
