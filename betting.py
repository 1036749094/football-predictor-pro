def kelly_bet(ev_label):

    if "高EV" in ev_label:
        return "建议下注资金：5%~8%"
    elif "正EV" in ev_label:
        return "建议下注资金：2%~4%"
    else:
        return "建议不下注"
