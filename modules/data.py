# data.py
from configparser import SafeConfigParser, RawConfigParser
from .fgui import fexplore
from .pcookie import pcookies
from termcolor import colored

def get():
    file = "../config/config.txt"
    file = fexplore()
    parser = SafeConfigParser()
    rparser = RawConfigParser()
    print(colored(f"Opening '{file}'...'", "green", attrs=["bold"]))
    parser.read(file)
    rparser.read(file)

    return ({
        "user-agent": str(parser.get("User Agent", "name")),
        "browser": str(parser.get("Browser", "type")),
        "cookies": pcookies(str(rparser.get("Cookies", "cookie"))),
        "url": str(parser.get("Website", "url")),
        "test-page": str(parser.get("Test Page", "use")),
        "path": str(file),
        "proxy": {
            "ip": str(parser.get("Proxy", "ip")),
            "port": str(parser.get("Proxy", "port"))
        }
    })
