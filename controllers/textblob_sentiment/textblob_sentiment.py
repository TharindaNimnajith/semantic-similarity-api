# importing textblob library
# used for processing textual data and nlp tasks
from textblob import TextBlob


# function to return textblob sentiment given a text
# textblob sentiment - tuple of form (polarity, subjectivity)
# polarity determines if a text expresses positive, negative or neutral sentiment
# polarity is a float within the range [-1.0, 1.0]
# where -1.0 is negative sentiment and 1.0 is positive sentiment
# subjectivity is a float within the range [0.0, 1.0]
# where 0.0 is very objective and 1.0 is very subjective
def evaluate(text):
    text_blob = TextBlob(text)
    return text_blob.sentiment
