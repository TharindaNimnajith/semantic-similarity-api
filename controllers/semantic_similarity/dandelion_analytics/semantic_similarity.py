# importing sys module
# used to access objects used or maintained by the interpreter and to functions
# that interact strongly with the interpreter
# import sys

# importing requests library
# used to send http requests using python
import requests

# importing secret values
from ..utility.config import secrets

# appending a relative path to the top package to the search path
# sys.path.append('../')

# dandelion text analysis api text similarity endpoint
endpoint = secrets.dandelion_endpoint

# dandelion text analysis api token
token = secrets.dandelion_token


# returning the semantic similarity score between two texts
def get_semantic_similarity(model_answer, student_answer, lang='en'):
    payload = {
        'token': token,
        'text1': model_answer,
        'text2': student_answer,
        'lang': lang,
        'bow': 'never'
    }

    try:
        return requests.get(endpoint,
                            params=payload).json()
    except:
        return 0


# returning the syntactic similarity score between two texts
def get_syntactic_similarity(model_answer, student_answer, lang='en'):
    payload = {
        'token': token,
        'text1': model_answer,
        'text2': student_answer,
        'lang': lang,
        'bow': 'always'
    }

    try:
        return requests.get(endpoint,
                            params=payload).json()
    except:
        return 0
