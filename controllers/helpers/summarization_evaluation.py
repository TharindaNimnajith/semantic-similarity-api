from difflib import SequenceMatcher

from .util.summarization_suggestions_enum import SummarizationSuggestions


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
        return SummarizationSuggestions.INSUFFICIENT
    if overall_score > 8:
        return SummarizationSuggestions.GOOD
    scores = (spelling_score,
              grammar_score,
              similarity_score,
              objectivity_score)
    index = scores.index(min(scores))
    if scores[index] == 0:
        return SummarizationSuggestions.SPELLING
    if scores[index] == 1:
        return SummarizationSuggestions.GRAMMAR
    if scores[index] == 2:
        return SummarizationSuggestions.RELEVANCY
    if scores[index] == 3:
        return SummarizationSuggestions.OBJECTIVITY
