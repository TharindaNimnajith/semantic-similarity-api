from . import semantic_similarity
from . import spelling_grammar_grammarbot
from . import textblob_sentiment


def evaluate(answers):
    model_answer = answers.model_answer
    student_answer = answers.student_answer
    spelling_score, grammar_score, matches = spelling_grammar_grammarbot.evaluate(student_answer)
    similarity_score = semantic_similarity.get_similarity(student_answer,
                                                          model_answer) * 10
    sentiment_scores = textblob_sentiment.evaluate(student_answer)
    objectivity_score = 10 - sentiment_scores.subjectivity * 10
    overall_score = calculate_overall_score(spelling_score,
                                            grammar_score,
                                            similarity_score,
                                            objectivity_score)
    return {
        'answers': {
            'model_answer': model_answer,
            'student_answer': student_answer
        },
        'overall': round(overall_score),
        'scores': {
            'spelling': round(spelling_score),
            'grammar': round(grammar_score),
            'similarity': round(similarity_score),
            'objectivity': round(objectivity_score)
        },
        'sentiment': {
            'polarity': sentiment_scores.polarity,
            'subjectivity': sentiment_scores.subjectivity
        },
        'matches': matches
    }


def calculate_overall_score(spelling_score, grammar_score, similarity_score, objectivity_score):
    overall_score = (spelling_score * 25 + grammar_score * 25 + similarity_score * 40 + objectivity_score * 10) / 100
    return overall_score
