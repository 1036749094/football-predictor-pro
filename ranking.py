def rank_bets(ev_data):

    ranked = []

    for k in ev_data:
        ranked.append((k, ev_data[k]["EV"]))

    ranked.sort(key=lambda x: x[1], reverse=True)

    return {
        "best": ranked[0],
        "all": ranked
    }
