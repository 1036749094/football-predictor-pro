def calc_ev(prob, odds):

    return {
        "home": {
            "EV": prob["home"] * odds["home"] - 1
        },
        "draw": {
            "EV": prob["draw"] * odds["draw"] - 1
        },
        "away": {
            "EV": prob["away"] * odds["away"] - 1
        }
    }
