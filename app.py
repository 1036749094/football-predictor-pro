import streamlit as st
from teams_db import teams
from model import xg_model, simulate
from odds_api import get_real_odds
from betting import analyze

st.title("⚽ V21 足球量化系统（真实赔率版）")

# ======================
# 输入球队
# ======================
home_team = st.selectbox("主队", list(teams.keys()))
away_team = st.selectbox("客队", list(teams.keys()))

api_key = st.text_input("Odds API Key（可选）")

if home_team != away_team:

    home = teams[home_team]
    away = teams[away_team]

    # ======================
    # 模型计算
    # ======================
    hxg, axg = xg_model(home, away)
    result = simulate(hxg, axg)

    st.subheader("⚽ 比赛概率")
    st.json(result)

    # ======================
    # 真实赔率
    # ======================
    odds = get_real_odds(home_team, away_team, api_key)

    st.subheader("💰 市场赔率")
    st.json(odds)

    # ======================
    # EV分析
    # ======================
    st.subheader("📊 价值投注分析")

    home_bet = analyze(result["home"], odds["home"])
    draw_bet = analyze(result["draw"], odds["draw"])
    away_bet = analyze(result["away"], odds["away"])

    st.json({
        "主胜": home_bet,
        "平局": draw_bet,
        "客胜": away_bet
    })

    # ======================
    # 最优选择
    # ======================
    best = max([
        ("主胜", home_bet["EV"]),
        ("平局", draw_bet["EV"]),
        ("客胜", away_bet["EV"])
    ], key=lambda x: x[1])

    st.success(f"🔥 最优投注：{best[0]}")
