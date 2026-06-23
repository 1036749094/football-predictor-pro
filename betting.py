def ev(prob, odds):
    return prob * (odds - 1) - (1 - prob)


def kelly(prob, odds):
    return max(0, ((odds - 1) * prob - (1 - prob)) / (odds - 1))


def recommendation(prob, odds):
    value = ev(prob, odds)
    stake = kelly(prob, odds)

    if value > 0.05 and stake > 0.03:
        signal = "🔥 强烈推荐下注"
    elif value > 0:
        signal = "⚡ 有价值下注"
    else:
        signal = "❌ 不建议下注"

    return {
        "EV": round(value, 4),
        "Kelly": round(stake, 4),
        "signal": signal
    }
