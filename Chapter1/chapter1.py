# In python3 urllib2 is same as urllib and well moduled
from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")

# BeautifulSoup instance. Feature is given to avoid warning
bsObj = BeautifulSoup(html.read(), features="html.parser")

# All 3 print statement print same result
# Print H1 text
print(bsObj.h1)

print(bsObj.body.h1)

print(bsObj.html.h1)
