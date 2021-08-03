from difflib import SequenceMatcher

from .util.paraphrasing_suggestions_enum import ParaphrasingSuggestions


def check_rule_violated(question_text,
                        answer_text):
    ratio = SequenceMatcher(None,
                            question_text,
                            answer_text).ratio()
    return ratio, ratio > 0.75


def finalize_marks(spelling_score,
                   grammar_score,
                   similarity_score,
                   objectivity_score,
                   comprehensiveness_score):
    if spelling_score < 3 and comprehensiveness_score < 3:
        similarity_score = similarity_score * 0.2 + comprehensiveness_score * 0.8
        objectivity_score = objectivity_score * 0.2 + comprehensiveness_score * 0.8
        return spelling_score, grammar_score, similarity_score, objectivity_score, comprehensiveness_score
    if comprehensiveness_score < 3:
        spelling_score = spelling_score * 0.2 + comprehensiveness_score * 0.8
        grammar_score = grammar_score * 0.2 + comprehensiveness_score * 0.8
        similarity_score = similarity_score * 0.2 + comprehensiveness_score * 0.8
        objectivity_score = objectivity_score * 0.2 + comprehensiveness_score * 0.8
        return spelling_score, grammar_score, similarity_score, objectivity_score, comprehensiveness_score
    if spelling_score < 3:
        similarity_score = similarity_score * 0.2 + spelling_score * 0.8
        objectivity_score = objectivity_score * 0.2 + spelling_score * 0.8
        return spelling_score, grammar_score, similarity_score, objectivity_score, comprehensiveness_score
    return spelling_score, grammar_score, similarity_score, objectivity_score, comprehensiveness_score


def calculate_overall_score(status,
                            spelling_score,
                            grammar_score,
                            similarity_score,
                            objectivity_score,
                            comprehensiveness_score):
    if status:
        overall_score = 2
    else:
        overall_score = (spelling_score * 10 +
                         grammar_score * 15 +
                         similarity_score * 50 +
                         comprehensiveness_score * 20 +
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
        return ParaphrasingSuggestions.COPIED.value
    if comprehensiveness_score < 3:
        return ParaphrasingSuggestions.INSUFFICIENT.value
    if overall_score > 8:
        return ParaphrasingSuggestions.GOOD.value
    scores = (spelling_score,
              grammar_score,
              similarity_score,
              objectivity_score)
    index = scores.index(min(scores))
    if index == 0:
        return ParaphrasingSuggestions.SPELLING.value
    if index == 1:
        return ParaphrasingSuggestions.GRAMMAR.value
    if index == 2:
        return ParaphrasingSuggestions.RELEVANCY.value
    return ParaphrasingSuggestions.OBJECTIVITY.value
