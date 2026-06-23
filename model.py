import math

def xg_model(home, away):
    home_xg = home["attack"] * away["defense"] * 1.2
    away_xg = away["attack"] * home["defense"] * 1.1
    return home_xg, away_xg


def poisson(lmbda, k):
    return (lmbda ** k) * math.exp(-lmbda) / math.factorial(k)


def simulate(home_xg, away_xg):
    max_goal = 5

    home_win = 0.0
    draw = 0.0
    away_win = 0.0

    for i in range(max_goal + 1):
        for j in range(max_goal + 1):
            p = poisson(home_xg, i) * poisson(away_xg, j)

            if i > j:
                home_win += p
            elif i == j:
                draw += p
            else:
                away_win += p

    return {
        "home": round(home_win, 4),
        "draw": round(draw, 4),
        "away": round(away_win, 4)
    }


def predict_match(home, away):
    home_xg, away_xg = xg_model(home, away)
    result = simulate(home_xg, away_xg)

    return {
        "home_xg": round(home_xg, 2),
        "away_xg": round(away_xg, 2),
        "home_win": result["home"],
        "draw": result["draw"],
        "away_win": result["away"]
    }
