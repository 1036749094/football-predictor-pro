def kelly(prob, odds):
    if odds <= 1:
        return 0
    return max(0, (prob * odds - 1) / (odds - 1))


def confidence_score(home, away):

    diff = abs(home["attack"] - away["attack"])

    score = 0.5 + diff * 0.2

    return round(min(score, 0.95), 2)
