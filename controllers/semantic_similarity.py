import requests

from .util import secrets

endpoint = secrets.dandelion_endpoint
token = secrets.dandelion_token


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
