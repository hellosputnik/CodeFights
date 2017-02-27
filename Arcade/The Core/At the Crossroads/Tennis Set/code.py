def tennisSet(score1, score2):
    return max(score1, score2) == 6 and min(score1, score2) <  5 or \
           max(score1, score2) == 7 and min(score1, score2) == 5 or \
           max(score1, score2) == 7 and min(score1, score2) == 6

