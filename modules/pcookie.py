from http.cookies import SimpleCookie
def pcookies(strcookie):
    cookie = SimpleCookie()
    cookie.load(strcookie)
    cookies = {}
    for key, morsel in cookie.items():
        cookies[key] = morsel.value
    return cookies
