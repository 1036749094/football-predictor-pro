import math

def xg_model(home, away):
    return (
        home["attack"] * away["defense"] * 1.2,
        away["attack"] * home["defense"] * 1.1
    )

def poisson(lmbda, k):
    return (lmbda ** k) * math.exp(-lmbda) / math.factorial(k)

def simulate(home_xg, away_xg):
    max_goal = 5
    home = draw = away = 0.0

    for i in range(max_goal + 1):
        for j in range(max_goal + 1):
            p = poisson(home_xg, i) * poisson(away_xg, j)
            if i > j:
                home += p
            elif i == j:
                draw += p
            else:
                away += p

    return {"home": home, "draw": draw, "away": away}

def predict_match(home, away):
    hx, ax = xg_model(home, away)
    r = simulate(hx, ax)

    return {
        "home_xg": round(hx, 2),
        "away_xg": round(ax, 2),
        "home_win": round(r["home"], 4),
        "draw": round(r["draw"], 4),
        "away_win": round(r["away"], 4),
    }
