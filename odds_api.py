import requests

# =========================
# 默认备用赔率（防止API失败）
# =========================
def fallback_odds():
    return {
        "home": 2.10,
        "draw": 3.20,
        "away": 3.60
    }


# =========================
# 真实赔率API（OddsAPI）
# =========================
def get_real_odds(home, away, api_key=None):

    # 如果没有API key → 用模拟
    if not api_key:
        return fallback_odds()

    try:
        url = "https://api.the-odds-api.com/v4/sports/soccer/odds/"
        
        params = {
            "apiKey": api_key,
            "regions": "eu",
            "markets": "h2h",
            "oddsFormat": "decimal"
        }

        res = requests.get(url, params=params)
        data = res.json()

        # 简化处理（取第一场比赛）
        match = data[0]

        odds = match["bookmakers"][0]["markets"][0]["outcomes"]

        return {
            "home": odds[0]["price"],
            "away": odds[1]["price"],
            "draw": odds[2]["price"] if len(odds) > 2 else 3.20
        }

    except:
        return fallback_odds()
