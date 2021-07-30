from .helpers import basic_metrics
from .helpers import paraphrasing_evaluation
from .helpers import semantic_similarity
from .helpers import spelling_grammar_grammarbot
from .helpers import text_preprocessing
from .helpers import textblob_sentiment


def evaluate(answers):
    student_answer_preprocessed = text_preprocessing.preprocess_text_basic(answers.student_answer)
    ratio, status = paraphrasing_evaluation.check_rule_violated(answers.question, student_answer_preprocessed)
    sentiment_scores = textblob_sentiment.evaluate(student_answer_preprocessed)
    objectivity_score = 10 - sentiment_scores.subjectivity * 10
    spelling_score, grammar_score, matches = spelling_grammar_grammarbot.evaluate(student_answer_preprocessed)
    similarity_score = semantic_similarity.get_similarity(student_answer_preprocessed,
                                                          answers.model_answer) * 10
    comprehensiveness_score = basic_metrics.get_comprehensiveness(answers.word_limit,
                                                                  answers.word_count)
    overall_score = paraphrasing_evaluation.calculate_overall_score(status,
                                                                    spelling_score,
                                                                    grammar_score,
                                                                    similarity_score,
                                                                    objectivity_score,
                                                                    comprehensiveness_score)
    suggestion = paraphrasing_evaluation.get_suggestions(status,
                                                         overall_score,
                                                         spelling_score,
                                                         grammar_score,
                                                         similarity_score,
                                                         objectivity_score,
                                                         comprehensiveness_score)
    return {
        'answers': {
            'question': answers.question,
            'word_limit': answers.word_limit,
            'word_count': answers.word_count,
            'model_answer': answers.model_answer,
            'student_answer': answers.student_answer
        },
        'sentiment': {
            'polarity': sentiment_scores.polarity,
            'subjectivity': sentiment_scores.subjectivity
        },
        'matches': matches,
        'scores': {
            'spelling': spelling_score,
            'grammar': grammar_score,
            'similarity': similarity_score,
            'comprehensiveness': comprehensiveness_score,
            'objectivity': objectivity_score
        },
        'overall': overall_score,
        'ratio': ratio,
        'suggestion': suggestion
    }
