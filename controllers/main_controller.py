from . import semantic_similarity
from . import spelling_grammar_grammarbot
from . import textblob_sentiment


def evaluate(answers):
    spelling_score, grammar_score, matches = spelling_grammar_grammarbot.evaluate(answers.student_answer)
    similarity_score = semantic_similarity.get_semantic_similarity(answers.student_answer,
                                                                   answers.model_answer)['similarity'] * 10
    sentiment_score = textblob_sentiment.evaluate(answers.student_answer)
    objectivity_score = 10 - sentiment_score.subjectivity * 10
    overall_score = calculate_overall_score(spelling_score,
                                            grammar_score,
                                            similarity_score,
                                            objectivity_score)
    return {
        'answers': {
            'model_answer': answers.model_answer,
            'student_answer': answers.student_answer
        },
        'overall': overall_score,
        'scores': {
            'spelling': spelling_score,
            'grammar': grammar_score,
            'similarity': similarity_score,
            'objectivity': objectivity_score
        },
        'sentiment': {
            'polarity': sentiment_score.polarity,
            'subjectivity': sentiment_score.subjectivity
        },
        'matches': matches
    }


def calculate_overall_score(spelling_score, grammar_score, similarity_score, objectivity_score):
    overall_score = (spelling_score * 6 + grammar_score * 10 + similarity_score * 10 + objectivity_score * 4) / 30
    return overall_score
