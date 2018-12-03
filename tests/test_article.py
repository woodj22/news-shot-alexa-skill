from article import article

def test_list_news_articles_as_urls():

    url = "https://www.bbc.co.uk/"

    url_list = article.list_news_articles_as_urls(url)

    assert type(url_list) is set
    for url in url_list:
        assert type(url) is str

def test_retrieve_news_article_as_string():

    url = 'www.bbc.co.uk'

    news_string = article.retrieve_news_article_as_string()
    assert isinstance(news_string, str) == 1
