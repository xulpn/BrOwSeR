import os
import time
def start():
    os.system("sudo systemctl start nginx")
    os.system("sudo cp -r ./www/* /var/www/html")

def stop():
    time.sleep(5)
    os.system("sudo systemctl stop nginx")
    os.system("sudo rm -rf /var/www/html/*")
