# browser.py
from selenium import webdriver
from .defaults import *
from .stealth import stealthy
def start_firefox(gdata):
    profile = webdriver.FirefoxProfile()
    profile.set_preference(firefox["set_prefrence"], gdata["user-agent"])
    browser = webdriver.Firefox(profile)
    browser.get(gdata["url"])
    for key, value in gdata["cookies"].items():
        browser.add_cookie({"name": key, "value": value})

def start_test_page(gdata):
    profile = make_profile(gdata["browser"])
    inject_user_agent(profile, gdata["browser"], gdata["user-agent"])
    if gdata["proxy"]["ip"] == "None" or gdata["proxy"]["port"] == "None":
        profile = stealthy(profile)
    else:
        profile = stealthy(profile, gdata["proxy"])

    browser = make_browser(profile, gdata["browser"])

    browser.get("http://localhost/")
    inject_cookies(browser, gdata["cookies"])
    browser.refresh()

def make_profile(browser_type):
    profile = None
    if browser_type == "Firefox":
        profile = webdriver.FirefoxProfile()
    return profile

def make_browser(profile, browser_type):
    browser = None
    if browser_type == "Firefox":
        browser = webdriver.Firefox(profile)
    return browser


def inject_user_agent(profile, browser_type, user_agent):
    if browser_type == "Firefox":
        profile.set_preference(firefox["set_prefrence"], user_agent)
    return profile

def inject_cookies(browser, cookies):
    for key, value in cookies.items():
        browser.add_cookie({"name": key, "value": value})
    return browser
