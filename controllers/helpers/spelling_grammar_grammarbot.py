from grammarbot import GrammarBotClient

client = GrammarBotClient()


def evaluate(text):
    try:
        res = client.check(text)
        matches = res.raw_json.get('matches')
        spelling_score, grammar_score = get_score(matches,
                                                  len(text.split()))
    except Exception as e:
        spelling_score, grammar_score, matches = 0, 0, []
        print(e)
    return spelling_score, grammar_score, matches


def get_score(matches,
              length):
    spelling_mistakes_count = 0
    grammar_mistakes_count = 0
    for match in matches:
        if match['rule']['issueType'] == 'misspelling':
            spelling_mistakes_count += 1
        else:
            grammar_mistakes_count += 1
    if spelling_mistakes_count == 0:
        spelling_score = 10
    else:
        spelling_score = (length - spelling_mistakes_count) * 7 / length
    if grammar_mistakes_count == 0:
        grammar_score = 10
    else:
        grammar_score = (length - grammar_mistakes_count) * 7 / length
    grammar_score = grammar_score * 0.7 + spelling_score * 0.3
    return spelling_score, grammar_score