import os
print("Setting up...\nSystem: Kali Linux \n Software: BrOwSeR_v1.0")
os.system("sudo apt update && sudo apt upgrade")
os.system("wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz");
os.system("tar -xvf geckodriver-v0.30.0-linux64.tar.gz");
os.system("sudo chmod +x geckodriver && sudo chmod BrOwSeR.desktop && sudo chmod +x main.py")
os.system("sudo cp geckodriver /usr/local/bin")
os.system("sudo rm -rf ./geckodriver*")

os.system("sudo apt install python-pip && pip install selenium termcolor")
os.system("sudo apt -y install wget gpg && sudo sh -c 'echo " + "deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main" + " > /etc/apt/sources.list.d/atom.list' && curl -fsSL https://packagecloud.io/AtomEditor/atom/gpgkey | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/atom-keyring.gpg && sudo apt update && sudo apt install atom")
os.system("atom .")
