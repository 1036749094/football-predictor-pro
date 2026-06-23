def calc_ev(result):
    home = result["home_win"]
    draw = result["draw"]
    away = result["away_win"]

    ev_score = (home * 1.9 + draw * 3.2 + away * 2.8) - 1

    if ev_score > 0.2:
        return "🔥 高EV（强烈推荐）"
    elif ev_score > 0:
        return "🟡 正EV（可下注）"
    else:
        return "🔴 负EV（不建议）"
