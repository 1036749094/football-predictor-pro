def ev(prob, odds):
    return prob * odds - 1


def kelly(prob, odds):
    return max(0, (prob * odds - 1) / (odds - 1))


def analyze(prob, odds):
    value = ev(prob, odds)
    stake = kelly(prob, odds)

    if value > 0.05:
        signal = "🔥 强烈价值投注"
    elif value > 0:
        signal = "⚡ 小额价值"
    else:
        signal = "❌ 无价值"

    return {
        "prob": round(prob, 4),
        "odds": odds,
        "EV": round(value, 4),
        "Kelly": round(stake, 4),
        "signal": signal
    }
