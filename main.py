from modules import *
import os


# @main
# Description:
#
#

def main():
    os.system("figlet BrOwSeR")
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
        else:
            run_main = True

        while (not run_main):
            if [ exit_p == True]:
                print("Exiting...")
                exit()
            continue

        main_br = browser.start_firefox(gdata)

    # for files in os.listdir(path):
    #     file = os.path.join(path, files)
    #     print(file)

main()
