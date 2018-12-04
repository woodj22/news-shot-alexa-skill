import pytest

from article import retrieve_article


def test_list_news_articles_as_urls():

    url = "https://www.bbc.co.uk/"

    url_list = retrieve_article.list_news_articles_as_urls(url)

    assert type(url_list) is list
    for url in url_list:
        assert type(url) is str


def test_retrieve_news_article_as_list():

    url = "https://www.bbc.co.uk/"

    article_suffix = retrieve_article.list_news_articles_as_urls(url)

    article_url = 'https://www.bbc.co.uk/' + article_suffix[0]
    print(article_url)
    news_string = retrieve_article.retrieve_news_article_as_list(article_url)

    assert type(news_string) is list
