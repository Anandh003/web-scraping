# CHAPTER 2 - Advanced HTML Parsing
from base import get_page

bs = get_page('http://www.pythonscraping.com/pages/warandpeace.html')

#findall(tag, attribute, recursive, text, limit, keywords)
names = bs.findAll('span', {'class': 'green'})

names = {name.get_text() for name in names}

for name in names:
    print(name)

"""
Other BS Objects
    Bs object   - Instance of BeautifulSoup
    Tag object  - Retrived in list or by calling find and findall functions
    navigableString object    - Used to represent string rather than tag
    comment object  -   used to find HTML comments
"""
