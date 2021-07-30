from .helpers import basic_metrics
from .helpers import paraphrasing_evaluation
from .helpers import semantic_similarity
from .helpers import spelling_grammar_grammarbot
from .helpers import text_preprocessing
from .helpers import textblob_sentiment
from .helpers.util.paraphrasing_suggestions_enum import ParaphrasingSuggestions


def evaluate(answers):
    student_answer_preprocessed = text_preprocessing.preprocess_text_basic(answers.student_answer)
    ratio, status = paraphrasing_evaluation.check_rule_violated(answers.question, student_answer_preprocessed)
    if not status:
        sentiment_scores = textblob_sentiment.evaluate(student_answer_preprocessed)
        objectivity_score = 10 - sentiment_scores.subjectivity * 10
        spelling_score, grammar_score, matches = spelling_grammar_grammarbot.evaluate(student_answer_preprocessed)
        similarity_score = semantic_similarity.get_similarity(student_answer_preprocessed,
                                                              answers.model_answer) * 10
        comprehensiveness_score = basic_metrics.get_comprehensiveness(answers.word_limit,
                                                                      answers.word_count)
        overall_score = paraphrasing_evaluation.calculate_overall_score(spelling_score,
                                                                        grammar_score,
                                                                        similarity_score,
                                                                        objectivity_score,
                                                                        comprehensiveness_score)
        suggestion = paraphrasing_evaluation.get_suggestions(overall_score,
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
                'spelling': round(spelling_score),
                'grammar': round(grammar_score),
                'similarity': round(similarity_score),
                'comprehensiveness': round(comprehensiveness_score),
                'objectivity': round(objectivity_score)
            },
            'overall': round(overall_score),
            'ratio': ratio,
            'suggestion': suggestion
        }
    else:
        return {
            'answers': {
                'question': answers.question,
                'word_limit': answers.word_limit,
                'word_count': answers.word_count,
                'model_answer': answers.model_answer,
                'student_answer': answers.student_answer
            },
            'sentiment': {
                'polarity': 0,
                'subjectivity': 0
            },
            'matches': [],
            'scores': {
                'spelling': 0,
                'grammar': 0,
                'similarity': 0,
                'comprehensiveness': 0,
                'objectivity': 0
            },
            'overall': 0,
            'ratio': ratio,
            'suggestion': ParaphrasingSuggestions.COPIED
        }
