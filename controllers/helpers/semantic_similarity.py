import requests

from .util import secrets

endpoint = secrets.dandelion_endpoint

token_1 = secrets.dandelion_token_1
token_2 = secrets.dandelion_token_2


def get_similarity(model_answer,
                   student_answer):
    try:
        response = get_semantic_similarity(model_answer,
                                           student_answer,
                                           token_1)
        if response != -1:
            if 'similarity' in response:
                return response['similarity']
        response = get_semantic_similarity(model_answer,
                                           student_answer,
                                           token_2)
        if response != -1:
            if 'similarity' in response:
                return response['similarity']
        else:
            return 0
    except Exception as e:
        print(e)
        return 0


def get_semantic_similarity(model_answer,
                            student_answer,
                            token,
                            lang='en'):
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
    except Exception as e:
        print(e)
        return -1


def get_syntactic_similarity(model_answer,
                             student_answer,
                             token,
                             lang='en'):
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
    except Exception as e:
        print(e)
        return -1
