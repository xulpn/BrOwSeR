#!/usr/bin/env python3
from modules import *
# @main
# Description
def main():

    display.title()
    display.start()
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
        display.note("See the test page if the right configuration is set!")
        con = input("continue (y/n): ")
        if con != 'y':
            print("Exiting...")
            exit()

        # main_br = browser.start_firefox(gdata)

    # for files in os.listdir(path):
    #     file = os.path.join(path, files)
    #     print(file)

main()
