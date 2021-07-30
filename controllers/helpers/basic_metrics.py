def get_comprehensiveness(word_limit,
                          word_count):
    if word_limit > 0:
        ratio = (word_count / word_limit) * 10
        if ratio > 7.5:
            return 10
        else:
            return ratio
    else:
        return 0
