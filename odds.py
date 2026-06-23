import requests

# 示例：手动赔率（默认 fallback）
def get_odds():
    return {
        "home": 2.10,
        "draw": 3.30,
        "away": 3.40
    }

# 如果你以后有 API（比如 OddsAPI）
def get_odds_api(api_key):
    url = f"https://api.the-odds-api.com/v4/sports/soccer/odds/?apiKey={api_key}"
    try:
        r = requests.get(url)
        return r.json()
    except:
        return get_odds()
