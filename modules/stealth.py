def set_proxy(profile, proxy_ip, proxy_port):
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", proxy_ip)
    profile.set_preference("network.proxy.http_port", int(proxy_port))
    profile.update_preferences()
    return profile

def remove_detectable_prefs(profile):
    profile.set_preference("dom.webdriver.enable", False)
    profile.set_preference("useAutomationExstension", False)
    profile.update_preferences()
    return profile;

def stealthy(profile, proxy=False):
    if proxy:
        profile = set_proxy(profile, proxy.ip, proxy.port)
    profile = remove_detectable_prefs(profile)
    return profile
