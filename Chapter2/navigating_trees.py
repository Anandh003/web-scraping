"""
    Navigating HTML DOM Trees
"""
import re
import sys
import os

sys.path.append(os.getcwd())

from base import get_page

def main():
    bs = get_page('http://www.pythonscraping.com/pages/page3.html')

    # Descendants vs Childerens
    # Children - exactly one tag below parent
    # Descendants - any level below parent
    # All children are descendants but not all descendants are children

    print('------------------Children-------------------')
    # Get Children
    for child in bs.find('table', {'id': 'giftList'}).children:
        print(child)

    print('------------------Next Siblings-------------------')
    # Get Next siblings (this print all rows except header 1st one)
    for sibling in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
        print(sibling)

    print('------------------Previous Siblings-------------------')
    # Get Next siblings (this print none because the selected row is 1st row)
    for sibling in bs.find('table', {'id': 'giftList'}).tr.previous_siblings:
        print(sibling)

    # Dealing with Parents
    print(bs.find(
        'img',{'src': '../img/gifts/img1.jpg'}
        ).parent.previous_sibling.get_text())

    # Regular Expressions and Beautiful Soup
    # Take <img src="../img/gifts/img3.jpeg">
    # Don't try to get this with help of tag or position use look for file path
    images = bs.find_all(
        'img', {'src': re.compile('\.\.\/img\/gifts\/img.*\.jpg')}
    )
    for image in images:
        print(image)

    # Lambda Experession
    # U can pass lambda expression function as argument to findall function
    attributes = bs.find_all(lambda tag: len(tag.attrs) == 2)
    print(20 * '*' + 'Tags with 2 attributest' + 20 * '*' + '\n', attributes)

if __name__ == '__main__':
    main()
