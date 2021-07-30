from difflib import SequenceMatcher

from .util.paraphrasing_suggestions_enum import ParaphrasingSuggestions


def check_rule_violated(question_text,
                        answer_text):
    ratio = SequenceMatcher(None,
                            question_text,
                            answer_text).ratio()
    return ratio, ratio > 0.9


def calculate_overall_score(spelling_score,
                            grammar_score,
                            similarity_score,
                            objectivity_score,
                            comprehensiveness_score):
    overall_score = (spelling_score * 20 +
                     grammar_score * 20 +
                     similarity_score * 40 +
                     comprehensiveness_score * 15 +
                     objectivity_score * 5) / 100
    return overall_score


def get_suggestions(overall_score,
                    spelling_score,
                    grammar_score,
                    similarity_score,
                    objectivity_score,
                    comprehensiveness_score):
    if comprehensiveness_score < 3:
        return ParaphrasingSuggestions.INSUFFICIENT
    if overall_score > 8:
        return ParaphrasingSuggestions.GOOD
    scores = (spelling_score,
              grammar_score,
              similarity_score,
              objectivity_score)
    index = scores.index(min(scores))
    if scores[index] == 0:
        return ParaphrasingSuggestions.SPELLING
    if scores[index] == 1:
        return ParaphrasingSuggestions.GRAMMAR
    if scores[index] == 2:
        return ParaphrasingSuggestions.RELEVANCY
    if scores[index] == 3:
        return ParaphrasingSuggestions.OBJECTIVITY
