import random

def get_odds():

    base = random.uniform(1.8, 2.4)

    return {
        "home": round(base, 2),
        "draw": round(base + 1.2, 2),
        "away": round(base + 1.0, 2)
    }
