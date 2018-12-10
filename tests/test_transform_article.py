from article import transform_article


def test_it_can_sort_array_of_words_into_frequency_dict():
    words = ['the', 'the', 'hello', 'the', 'world']

    sorted_words = transform_article.sort_list_of_words_into_frequency(words)

    assert sorted_words == [('the', 3), ('hello', 1), ('world', 1)]


def test_it_can_filter_list_of_words_by_common_words():
    common_words = ('the', 'pop', 'i', 'a')

    words = ['the', 'i', 'list', 'jesus', 'common', 'words', 'words', 'i', 'a']

    filtered_words = transform_article.filter_list_of_words_by_common_words(words, common_words)

    for word in common_words:
        assert word not in filtered_words


def test_it_returns_true_if_a_word_is_in_a_list_of_common_words():
    common_words = ('the', 'pop', 'i', 'a')

    word = 'the'

    is_in_list = transform_article.word_is_in_list(word, common_words)

    assert is_in_list is True


def test_it_returns_false_if_a_word_is_not_in_a_list_common_words():
    common_words = ('the', 'pop', 'i', 'a')

    word = 'not_in_common_words'

    is_in_list = transform_article.word_is_in_list(word, common_words)

    assert is_in_list is False


def test_it_can_split_list_of_sentences_into_list_of_lowercase_words():

    list_of_sentences = [
        'The UK',
        'little john',
        'urban living'

     ]

    word_list = transform_article.split_list_of_sentences_into_list_of_lowercase_words(list_of_sentences)

    assert type(word_list) is list

    assert ['the', 'uk', 'little', 'john', 'urban', 'living'] == word_list
