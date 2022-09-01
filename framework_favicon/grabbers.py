from .database import database
from .grab_result import GrabResult, Status

def grab_favicon_from_md5(md5: str) -> GrabResult:
    if md5 in database.framworks:
        return GrabResult(Status.STATUS_OK, database.framworks[md5])
    else:
        return GrabResult(Status.STATUS_NOT_FOUND, '')

def grab_favicon_from_data(data:str) -> GrabResult:
    import hashlib
    return grab_favicon_from_md5(hashlib.md5(data))

def grab_favicon_from_file(file:str) -> GrabResult:
    import urllib.request
    with urllib.request.urlopen(file) as f:
        return grab_favicon_from_data(f.read().decode('utf-8'))

def try_grab_favicon_from_file(file:str) -> GrabResult:
    try:
        return grab_favicon_from_file(file)
    except:
        return GrabResult(Status.STATUS_NOT_FOUND, '')

def grab_favicon_from_website(url: str) -> GrabResult:
    import urllib
    from urllib.parse import urlparse
    from bs4 import BeautifulSoup
    page = urllib.urlopen(url)
    soup = BeautifulSoup(page)
    icon_link = soup.find("link", rel="shortcut icon")
    def is_absolute(url):
        return bool(urlparse.urlparse(url).netloc)
    if not is_absolute(url):
        import os
        icon_link = os.path.join(url, icon_link)
    return grab_favicon_from_file(icon_link)

def try_grab_favicon_from_website(url:str) -> GrabResult:
    try:
        return grab_favicon_from_website(url)
    except:
        return GrabResult(Status.STATUS_NOT_FOUND, '')

