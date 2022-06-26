from googlesearch import search
import requests
from bs4 import BeautifulSoup


def google_search(keyword='', nr_results=10, pause=2.0):
    """
    Get list of website address, google search result based on specific keyword.

    :param keyword: Key word to query.
    :param nr_results: Number of desired result.
    :param pause: Wait time between requests.
    :return: Iterator, each item is a string, website address.
    """
    # TODO: Try out google-api-client-python to see the differences.
    return search(query=keyword,  # Query string
                  tld='com',  # Top level domain
                  # lang='en',  # Language
                  tbs='0',  # Time limits
                  safe='off',  # Safe search
                  num=10,  # Number of results per page
                  start=0,  # First result to retrieve
                  stop=nr_results,  # Last result to retrieve
                  pause=pause,  # Lapse to wait between requests. Too short = Google to block IP
                  country='')  # Country or region to focus the search on


def get_website_description(url='', get_all=True):
    """
    Perform google search based on specific keyword.
    :param url: String, website address.
    :param get_all: If True, get all available description from html text.
    :return: A string description of the webpage. If not available, return empty string.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    metas = soup.find_all('meta')
    if get_all:
        # Get all available description
        return ''.join([m.get('content') for m in metas if m.get('name') == 'description'])
    else:
        # Get only 1 description, some website has too long of description, which takes time to get all.
        desc = ''
        for m in metas:
            if m.get('name') == 'description':
                desc = m.get('content')
                break
        return desc


def create_result_dict(urls, get_all=True):
    output = dict()
    for uid, url in enumerate(urls):
        data = {
            'link': url,
            'description': get_website_description(url, get_all=get_all)
        }
        output['search_result_%d' % uid] = data
    return output


if __name__ == '__main__':
    res = google_search(keyword='Bosch', nr_results=10)
    print(create_result_dict(res, get_all=False))
