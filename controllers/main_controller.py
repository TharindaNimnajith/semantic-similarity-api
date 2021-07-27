from . import semantic_similarity
from . import spelling_grammar_grammarbot
from . import textblob_sentiment


def evaluate(answers):
    model_answer = answers.model_answer
    student_answer = answers.student_answer
    spelling_score, grammar_score, matches = spelling_grammar_grammarbot.evaluate(student_answer)
    similarity_score = semantic_similarity.get_semantic_similarity(student_answer,
                                                                   model_answer)['similarity'] * 10
    sentiment_score = textblob_sentiment.evaluate(student_answer)
    objectivity_score = 10 - sentiment_score.subjectivity * 10
    overall_score = calculate_overall_score(spelling_score,
                                            grammar_score,
                                            similarity_score,
                                            objectivity_score)
    return {
        'answers': {
            'model_answer': model_answer,
            'student_answer': student_answer
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
    overall_score = (spelling_score * 25 + grammar_score * 25 + similarity_score * 40 + objectivity_score * 10) / 100
    return overall_score
