import random
import re
import sys
import os
from urllib.parse import urlparse

sys.path.append(os.getcwd())

from base import get_page

# Gets internal links
def get_internal_links(bs, include_url):
    include_url = "{}://{}".format(
        urlparse(include_url).scheme, urlparse(include_url).netloc
    )
    links = bs.find_all('a', href=re.compile('^(/|.*' + include_url + ')'))
    internal_links = []

    for link in links:
        if (
            link.attrs.get('href', None)
            and link.attrs['href'] not in internal_links
        ):
            if link.attrs['href'].startswith('/'):
                internal_links.append(include_url + link.attrs['href'])
            else:
                internal_links.append(link.attrs['href'])

    return internal_links

# Gets external links
def get_external_links(bs, exclude_url):
    external_links = []
    links = bs.find_all('a', href=re.compile(
        f'^(http|www)((?!{exclude_url}).)*$')
    )

    for link in links:
        if (
            link.attrs.get('href', None)
            and link.attrs['href'] not in external_links
        ):
            external_links.append(link.attrs['href'])

    return external_links


# Recursively gets external link. If external link not found, move around
# the website and search for external link
def get_random_external_links(home_url):
    if not  home_url:
        return None

    bs = get_page(home_url)

    if not bs:
        return None

    external_links = get_external_links(bs, urlparse(home_url).netloc)

    if not external_links:
        print('No External Links Found!!, Looking around the site for one')
        domain = f"{urlparse(home_url).scheme}://{urlparse(home_url).netloc}"
        internal_link = get_internal_links(bs, domain)
        if not internal_link:
            print('No Internal Links Found!!')
            return None

        external_link = get_random_external_links(
            internal_link[random.randint(0, len(internal_link) - 1)]
        )
        return external_link
    else:
        return external_links[random.randint(0, len(external_links) - 1)]


# Gets external links recursively
def get_external_links_only(home_url):
    if home_url is None:
        return

    external_link = get_random_external_links(home_url)
    print(f'External Links: {external_link}')
    get_external_links_only(external_link)


def main():
    get_external_links_only("https://www.sesamestreet.org/")


if __name__ == "__main__":
    main()
