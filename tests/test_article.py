import pytest

from article import article

def test_list_news_articles_as_urls():

    url = "https://www.bbc.co.uk/"

    url_list = article.list_news_articles_as_urls(url)

    assert type(url_list) is list
    for url in url_list:
        assert type(url) is str

@pytest.mark.skip(reason="Not finished yet.")
def test_retrieve_news_article_as_string():

    url = "https://www.bbc.co.uk/"

    article_suffix = article.list_news_articles_as_urls(url)
    article_url = 'https://www.bbc.co.uk/' + article_suffix[0]

    news_string = article.retrieve_news_article_as_string(article_url)

    assert type(news_string) is str


def test_it_can_sort_array_of_words_into_frequnecy_dict():
    words = ['the', 'the', 'hello', 'the', 'world']
    sorted_words = article.sort_array_of_words_into_frequency(words)
    # assert sorted_words == [('the', 3), ('hello', 1), ('world', 1)]
    assert sorted_words == {'the': 3, 'hello': 1, 'world': 1}


def test_it_can_filter_list_of_words_by_common_words():
    common_words = ('the', 'pop', 'i', 'a')
    words = ['the', 'i', 'list', 'jesus', 'common', 'words', 'words', 'i', 'a']
    filtered_words = article.filter_list_of_words_by_common_words(words, common_words)
    for word in common_words:
        assert word not in filtered_words