from urllib.request import urlopen
from urllib.error import HTTPError, URLError

from bs4 import BeautifulSoup


def get_title(url):
    try:
        html = urlopen(url)
    # HTTPError is general for both 500 and 400 errors
    except HTTPError as e:
        return None
    # URLError is specific to server not found error
    except URLError as e:
        return None

    try:
        bs = BeautifulSoup(html.read(), features='html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None

    return title

title = get_title("http://www.pythonscraping.com/exercises/exercise1.html")
if not title:
    print('Title is Not found')
else:
    print(title)
