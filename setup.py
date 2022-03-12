import os
print("Upgrading OS...")
os.system("sudo apt update && sudo apt upgrade")
os.system("wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz -O ~/Downloads/geckodriver");
os.system("chmod +x ~/Downloads/geckodriver")
os.system("cp ~/Downloads/geckodriver /usr/local/bin")
