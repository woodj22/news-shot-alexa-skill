import json
import csv

from article.retrieve_article import *
from article.transform_article import *


def handle(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    base_url = "https://www.bbc.co.uk/"

    css_class_name = 'story-body__inner'

    articles_urls = list_news_articles_as_urls(base_url)

    common_words = read_common_words('../common-words.csv')

    for url in articles_urls:
        article_sentences = dump_news_article_main_body_into_list_of_sentences(base_url + url, css_class_name)

        words = split_list_of_sentences_into_list_of_lowercase_words(article_sentences)

        filtered_words = filter_list_of_words_by_common_words(words, common_words)

        ten_most_frequent_words = sort_list_of_words_into_frequency(filtered_words)[:10]

        print(ten_most_frequent_words)

    return response


def read_common_words(csv_path):
    with open(csv_path, 'r') as csvfile:
        your_list = csv.reader(csvfile, delimiter=',')
        return list(your_list)[0]
