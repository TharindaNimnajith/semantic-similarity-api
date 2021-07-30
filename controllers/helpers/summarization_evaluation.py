from difflib import SequenceMatcher

from .util.summarization_suggestions_enum import SummarizationSuggestions


def check_rule_violated(question_text,
                        answer_text):
    ratio = SequenceMatcher(None,
                            question_text,
                            answer_text).ratio()
    return ratio, ratio > 0.8


def calculate_overall_score(status,
                            spelling_score,
                            grammar_score,
                            similarity_score,
                            objectivity_score,
                            comprehensiveness_score):
    if status:
        overall_score = 2
    else:
        overall_score = (spelling_score * 15 +
                         grammar_score * 20 +
                         similarity_score * 35 +
                         comprehensiveness_score * 25 +
                         objectivity_score * 5) / 100
    return overall_score


def get_suggestions(status,
                    overall_score,
                    spelling_score,
                    grammar_score,
                    similarity_score,
                    objectivity_score,
                    comprehensiveness_score):
    if status:
        return SummarizationSuggestions.COPIED.value
    if comprehensiveness_score < 3:
        return SummarizationSuggestions.INSUFFICIENT.value
    if overall_score > 8:
        return SummarizationSuggestions.GOOD.value
    scores = (spelling_score,
              grammar_score,
              similarity_score,
              objectivity_score)
    index = scores.index(min(scores))
    if index == 0:
        return SummarizationSuggestions.SPELLING.value
    if index == 1:
        return SummarizationSuggestions.GRAMMAR.value
    if index == 2:
        return SummarizationSuggestions.RELEVANCY.value
    return SummarizationSuggestions.OBJECTIVITY.value
