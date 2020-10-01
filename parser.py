import requests
import bs4

URL = ""
HEADERS = {}

def get_html(url, params = None):
    r = requests.get(url, headers = HEADERS, params = params)
    return r

def 
