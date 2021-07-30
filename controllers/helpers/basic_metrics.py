def get_comprehensiveness(word_limit,
                          word_count):
    ratio = (word_count / word_limit) * 10
    if ratio > 7.5:
        return 10
    else:
        return ratio
