
def split_list_of_sentences_into_list_of_lowercase_words(list_of_sentences):
    return [word.lower() for sentences in list_of_sentences for word in sentences.split()]


def sort_list_of_words_into_frequency(words):
    new_words = {}
    for word in words:
        if word not in new_words:
            new_words[word] = 1
        else:
            new_words[word] += 1

    return new_words


def filter_list_of_words_by_common_words(words, common_words):
    new_words = []
    for word in words:
        if word not in common_words:
            new_words.append(word)

    return new_words


def word_is_in_list(word, common_words):
    if word in common_words:
        return True
    else:
        return False
