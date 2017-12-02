#!/usr/bin/env python

import argparse

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

TEXT = "text"


def get_sentiment(client, text):
    # Create a document
    document = types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)

    # Detect the sentiment of the text
    return client.analyze_sentiment(document=document).document_sentiment


if __name__ == '__main__':
    # Parse cli args
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--text", required=True, dest=TEXT, help="Text for analysis")
    args = vars(parser.parse_args())

    # Instantiate a client
    client = language.LanguageServiceClient()

    text = args[TEXT]
    sentiment = get_sentiment(client, text)

    print('Text: {}'.format(text))
    print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
