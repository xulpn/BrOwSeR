# BrOwSeR_v1.0

## Features
#### New
- Configuration file (BrOwSeR/config/config.txt)
  - Added proxy option
#### Old
- Configuration file (BrOwSeR/config/config.txt)
  - Change User agent
  - Change cookies

# Requirements
- Operating System
  - Debian Based Linux (i.e: Ubuntu, Kali, Mint, etc)

# Getting started
- Click BrOwSeR.desktop file
- Run setup.py
```bash
python3 setup.py
```
- Create a configuration file and save it
```
[Browser]
type: Firefox

[User Agent]
name: <PUT-USER-AGENT-HERE->
example: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36

[Cookies]
cookie:<PUT-COOKIES-HERE>
example: nsid=s%2; login_email=me@e.com id_token=23;

[Website]
url: <PUT-WEBSITE-HERE>
example: https://www.google.com

[Test Page]
use: yes
example: yes or no

[Proxy]
ip: <PUT-IP-ADDRESS-HERE->
example: None or 121.122.123.124

port: <PUT-PORT-NUMBER-HERE>
example: None or 1234
```
- Run main.py
```bash
python3 main.py
```
- Choose saved configuration files
- Browser should launch with test page
- Coninue with coice "y" if configuration file is set correctly
- That's it for this latest version.
