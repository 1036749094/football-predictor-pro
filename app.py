def ev(prob, odds):
    """
    期望收益 EV
    EV > 0 才是正收益下注
    """
    return prob * (odds - 1) - (1 - prob)


def kelly(prob, odds):
    """
    凯利公式（控制下注比例）
    """
    if odds <= 1:
        return 0

    return max(0, ((odds - 1) * prob - (1 - prob)) / (odds - 1))


def recommendation(prob, odds):
    """
    投注建议系统（核心V18）
    """

    value = ev(prob, odds)
    stake = kelly(prob, odds)

    if value > 0.05 and stake > 0.03:
        signal = "🔥 强烈推荐下注"
    elif value > 0:
        signal = "⚡ 有价值下注"
    else:
        signal = "❌ 不建议下注"

    return {
        "probability": round(prob, 4),
        "odds": odds,
        "EV": round(value, 4),
        "Kelly": round(stake, 4),
        "signal": signal
    }


def best_option(results):
    """
    从多个市场中选最优EV
    """
    return max(results, key=lambda x: x["EV"])
