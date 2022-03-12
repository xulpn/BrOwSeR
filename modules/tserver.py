import os
def start():
    os.system("sudo systemctl stop nginx")
    os.system("sudo rm -rf /var/www/html/*")
    os.system("sudo cp -r ./www/* /var/www/html")
    os.system("sudo systemctl start nginx")
