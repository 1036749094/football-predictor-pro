import math

# =========================
# xG模型（简化版泊松基础）
# =========================

def xg_model(home, away):

    # 基础进攻 vs 防守
    home_xg = home["attack"] * away["defense"] * 1.2
    away_xg = away["attack"] * home["defense"] * 1.1

    return home_xg, away_xg


# =========================
# 泊松分布
# =========================

def poisson(lmbda, k):
    return (lmbda ** k) * math.exp(-lmbda) / math.factorial(k)


# =========================
# 比赛模拟（0-5球）
# =========================

def simulate(home_xg, away_xg):

    max_goals = 5

    home_win = 0
    draw = 0
    away_win = 0

    for i in range(max_goals + 1):
        for j in range(max_goals + 1):

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
