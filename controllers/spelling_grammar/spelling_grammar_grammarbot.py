# importing re module
# used to support regular expressions
import re
# importing punctuations from collection of string constants
from string import punctuation

# importing grammarbot library
from grammarbot import GrammarBotClient

client = GrammarBotClient()


# function to evaluate grammar and spelling of a given text
# and return grammar score, spelling score and grammatical and
# spelling mistakes identified
def evaluate(text):
    # perform basic text preprocessing
    text = preprocess_text(text)

    # check text for grammatical errors
    res = client.check(text)

    # raw json response for grammar or spelling rule violations
    matches = res.raw_json.get('matches')

    spelling_score, grammar_score = get_score(matches, len(text.split()))

    return spelling_score, grammar_score, matches


# function to calculate grammar and spelling score for a given text input
# based on the grammar and spelling mistake count of the text
def get_score(matches, length):
    spelling_mistakes_count = 0
    grammar_mistakes_count = 0

    for match in matches:
        if match['rule']['issueType'] == 'misspelling':
            spelling_mistakes_count += 1
        else:
            grammar_mistakes_count += 1

    if spelling_mistakes_count == 0:
        spelling_score = 10.0
    else:
        spelling_score = (length - spelling_mistakes_count) * 7.5 / length

    if grammar_mistakes_count == 0:
        grammar_score = 10.0
    else:
        grammar_score = (length - grammar_mistakes_count) * 7.5 / length

    return spelling_score, grammar_score


# function to preprocess a given text
def preprocess_text(text):
    text = str(text.strip())
    text = remove_html(text)
    text = remove_punctuation(text)
    text = replace_contractions(text)
    return text


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
