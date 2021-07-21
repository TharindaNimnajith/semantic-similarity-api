# importing json which is a python built-in package
# used to work with json data
# import json

# importing spelling_grammar module from dandelion_analytics module in
# semantic_similarity package
from .semantic_similarity.dandelion_analytics import semantic_similarity
# importing spelling_grammar_grammarbot module from spelling_grammar package
from .spelling_grammar import spelling_grammar_grammarbot
# importing spelling_grammar_grammarbot module from spelling_grammar package
from .textblob_sentiment import textblob_sentiment


# function to return evaluation scores for the provided student answer
def evaluate(answers):
    spelling_score, grammar_score, matches = spelling_grammar_grammarbot.evaluate(answers.student_answer)
    similarity_score = semantic_similarity.get_semantic_similarity(answers.student_answer,
                                                                   answers.model_answer)
    sentiment_score = textblob_sentiment.evaluate(answers.student_answer)
    overall_score = calculate_overall_score(spelling_score,
                                            grammar_score,
                                            similarity_score['similarity'])
    return {
        'answers': {
            'model_answer': answers.model_answer,
            'student_answer': answers.student_answer
        },
        'overall': overall_score,
        'scores': {
            'spelling': spelling_score,
            'grammar': grammar_score,
            'similarity': similarity_score['similarity'] * 10.0
        },
        'sentiment': {
            'polarity': sentiment_score.polarity,
            'subjectivity': sentiment_score.subjectivity
        },
        'matches': matches
    }


# function to calculate overall score for the provided student answer
def calculate_overall_score(spelling_score, grammar_score, similarity_score):
    overall_score = round((spelling_score + grammar_score + similarity_score) / 3.0)
    return overall_score
