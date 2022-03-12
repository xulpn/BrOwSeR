# data.py
from configparser import SafeConfigParser, RawConfigParser
from .fgui import fexplore
from .pcookie import pcookies
def get():
    file = "../config/config.txt"
    if [input("Choose folder (Y/n): ") == "Y"]:
        file = fexplore()
    parser = SafeConfigParser()
    rparser = RawConfigParser()
    print(f"Opening '{file}'...'")
    parser.read(file)
    rparser.read(file)

    return ({
        "user-agent": str(parser.get("User Agent", "name")),
        "browser": str(parser.get("Browser", "type")),
        "cookies": pcookies(str(rparser.get("Cookies", "cookie"))),
        "url": str(parser.get("Website", "url")),
        "test-page": str(parser.get("Test Page", "use")),
        "path": str(file)
    })
