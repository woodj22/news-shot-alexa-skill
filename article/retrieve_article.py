import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
session = HTMLSession()


def retrieve_news_article_as_string(article_url):
    session = HTMLSession()

    r = session.get(article_url)
    # print(r.html.text)
    txt = r.html.find('#story-body', first=True)
    print(txt.find('p'))

    # soup = BeautifulSoup(request.content, 'html.parser')
    # mydivs = soup.find("div", {"class": "column--primary"})

    return 'erfd'


def list_news_articles_as_urls(base_url, news_site_suffix='news'):
    url = base_url + news_site_suffix
    class_name = 'gel-layout gel-layout--equal'
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')
    soup = soup.find("div", {"class" : class_name})
    main_article_href = soup.find("a", {"class": 'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold nw-o-link-split__anchor'})['href']
    response = soup.find_all("a", {"class": "gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor"})

    links = []
    for r in response:
        links.append(r['href'])

    links.append(main_article_href)

    return links


