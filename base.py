"""
    Base Script to have reusable functions
"""

from urllib.error import HTTPError, URLError
from urllib.request import urlopen

from bs4 import BeautifulSoup

def get_page(url):
    try:
        resp = urlopen(url)
    except HTTPError as e:
        print('Unable to fetch {}'.format(url))
        print('Error Message \n {}'.format(e))
        return None
    except URLError as e:
        print('Unable to fetch {}'.format(url))
        print('Error Message: {}'.format(e))
        return None

    return BeautifulSoup(resp, features="html.parser")


    
