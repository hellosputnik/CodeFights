def electionsWinners(votes, k):
    leader = max(votes)
    count  = 0

    # Handle special case where there are no votes left.
    if k == 0:
        return 1 if votes.count(leader) == 1 else 0

    for vote in votes:
        if vote + k > leader:
            count += 1

    return count

