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
        if length > 0:
            spelling_score = (length - spelling_mistakes_count) * 7 / length
        else:
            spelling_score = 0
    if grammar_mistakes_count == 0:
        grammar_score = 10
    else:
        if length > 0:
            grammar_score = (length - grammar_mistakes_count) * 7 / length
        else:
            grammar_score = 0
    if spelling_score > 5:
        grammar_score = grammar_score * 0.7 + spelling_score * 0.3
    elif spelling_score > 3.5:
        grammar_score = grammar_score * 0.4 + spelling_score * 0.6
    elif spelling_score < 2:
        grammar_score = grammar_score * 0.2 + spelling_score * 0.8
    elif spelling_score < 0.5:
        grammar_score = grammar_score * 0.1 + spelling_score * 0.9
    else:
        grammar_score = 0
    return spelling_score, grammar_score
