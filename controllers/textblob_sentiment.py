from textblob import TextBlob


def evaluate(text):
    text_blob = TextBlob(text)
    return text_blob.sentiment
