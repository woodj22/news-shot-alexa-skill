import requests
from bs4 import BeautifulSoup


def dump_news_article_main_body_into_list_of_sentences(article_url, body_class_name):
    r = requests.get(article_url)

    soup = BeautifulSoup(r.content, 'html.parser')

    try:
        main_text = soup.find("div", {"class": body_class_name}).findAll('p')
    except AttributeError:
        return []

    return [sentence.get_text() for sentence in main_text]


def list_news_articles_as_urls(base_url, news_site_suffix='news'):
    url = base_url + news_site_suffix
    class_name = 'gel-layout gel-layout--equal'
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')
    soup = soup.find("div", {"class": class_name})
    main_article_href = soup.find("a", {"class": 'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold nw-o-link-split__anchor'})['href']
    response = soup.find_all("a", {"class": "gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor"})

    links = []
    for r in response:
        links.append(r['href'])

    links.append(main_article_href)

    return links


