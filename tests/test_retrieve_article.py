from article import retrieve_article


def test_list_news_articles_as_urls():
    url = "https://www.bbc.co.uk/"

    url_list = retrieve_article.list_news_articles_as_urls(url)

    assert type(url_list) is list
    for url in url_list:
        assert type(url) is str


def test_it_can_dump_news_article_main_body():
    url = "https://www.bbc.co.uk/"

    article_suffix = retrieve_article.list_news_articles_as_urls(url)

    article_url = 'https://www.bbc.co.uk/' + article_suffix[0]

    class_name = 'story-body__inner'

    news_string = retrieve_article.dump_news_article_main_body_into_list_of_sentences(article_url, class_name)
    print(news_string)
    assert type(news_string) is list
