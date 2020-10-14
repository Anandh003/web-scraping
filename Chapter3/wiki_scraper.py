# import random
import re
import sys
import os

sys.path.append(os.getcwd())

from base import get_page


# def get_link(url = ''):
#     BASE_URL = f'http://en.wikipedia.org/{url}'

#     bs_obj = get_page(BASE_URL)

#     # Main content is with in div with 'bodycontent' id
#     return bs_obj.find('div', {'id': 'bodyContent'}).find_all(
#         'a', href=re.compile('^(/wiki/)((?!:).)*$')
#     )

# def main():

#     link = get_link('wiki/Kevin_Bacon')
    
#     while len(link) > 0:
#         new_article = link[random.randint(0, len(link) - 1)].attrs['href']
#         print(new_article)
#         link = get_link(new_article)

    # Returns all the links in the page.
    # for link in bs_obj.find_all('a'):
    #     if 'href' in link.attrs:
    #         print(link['href'])


# Recursive hop from one page to another
# def get_links(pages, url=''):
#     url = f'http://en.wikipedia.org/{url}'
#     bs_obj = get_page(url)
#     links = bs_obj.find_all('a', href=re.compile('^(/wiki/)'))
#     for link in links:
#         if 'href' in link.attrs and link.attrs['href'] not in pages:
#             new_page = link.attrs['href']
#             print(new_page)
#             pages.add(new_page)
#             get_links(pages, new_page)

# Gather data in pages
def get_links(pages, url=''):
    url = f'http://en.wikipedia.org/{url}'
    bs_obj = get_page(url)
    try:
        print(bs_obj.h1.get_text())
        print(bs_obj.find('', {'id': 'mw-content-text'}).find_all('p')[0].get_text())
        print(bs_obj.find('', {'id': 'ca-edit'}).find(
            'span').find('a').attrs['href'])
    except AttributeError as e:
        print('this link is missing something! Continuing')

    for link in bs_obj.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs and link.attrs['href'] not in pages:
            new_section = link.attrs['href']
            print('-'*30 + '\n' + new_section)
            pages.add(new_section)
            get_links(pages, new_section)
            

def main():
    pages = set()
    get_links(pages)


if __name__ == "__main__":
    main()    