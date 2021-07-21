# importing re module
# used to support regular expressions
import re
# importing punctuations from collection of string constants
from string import punctuation

# importing wordnet lemmatizer from nltk stem package
# used to remove morphological affixes from words, leaving only the word
# stem wordnet lemmatizer lemmatizes using built-in morphy function
# of wordnet
from nltk.stem import WordNetLemmatizer
# importing word tokenizer from nltk tokenizer package
# used for dividing strings into lists of substrings or tokens
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()


# function to preprocess a given text
def preprocess_text(text):
    tokens = tokenize_text(text)
    q1 = ' '.join(str(lemmatize_token(token)) for token in tokens)
    q2 = ' '.join(str(token) for token in tokens)
    return q1, q2


# function to remove html tags from a given text
def remove_html(sentence):
    return re.sub(re.compile('<.*?>'), ' ', sentence)


# function to remove punctuations from a given text
def remove_punctuation(sentence):
    return sentence.translate(str.maketrans(dict.fromkeys(punctuation)))


# function to replace specific contractions from a given text
def replace_specific_contractions(sentence):
    sentence = re.sub(r'won\'t', 'will not', sentence)
    sentence = re.sub(r'can\'t', 'can not', sentence)
    return sentence


# function to replace general contractions from a given text
def replace_general_contractions(sentence):
    sentence = re.sub(r'n\'t', ' not', sentence)
    sentence = re.sub(r'\'re', ' are', sentence)
    sentence = re.sub(r'\'s', ' is', sentence)
    sentence = re.sub(r'\'d', ' would', sentence)
    sentence = re.sub(r'\'ll', ' will', sentence)
    sentence = re.sub(r'\'t', ' not', sentence)
    sentence = re.sub(r'\'ve', ' have', sentence)
    sentence = re.sub(r'\'m', ' am', sentence)
    return sentence


# function to replace contractions from a given text
def replace_contractions(sentence):
    sentence = replace_specific_contractions(sentence)
    sentence = replace_general_contractions(sentence)
    return sentence


# function to preprocess a given text and return
# preprocessed set of tokens
def tokenize_text(text):
    text = str(text.lower())
    text = remove_html(text)
    text = remove_punctuation(text)
    text = replace_contractions(text)
    tokens = word_tokenize(text)
    tokens = remove_stopwords(tokens)
    return tokens


# function to convert a given toke to its lemma
def lemmatize_token(token):
    return lemmatizer.lemmatize(token)
