import streamlit as st
from teams_db import teams
from model import xg_model, simulate
from odds_api import get_odds
from ev_engine import calc_ev
from ranking import rank_bets
from risk import kelly, confidence_score

st.set_page_config(page_title="V24足球交易系统", layout="wide")

st.title("⚽ V24 足球量化交易系统（专业分析版）")

# ======================
# 输入比赛
# ======================
home_team = st.selectbox("主队", list(teams.keys()))
away_team = st.selectbox("客队", list(teams.keys()))

if home_team != away_team:

    home = teams[home_team]
    away = teams[away_team]

    # ======================
    # 模型预测
    # ======================
    hxg, axg = xg_model(home, away)
    prob = simulate(hxg, axg)

    st.subheader("📊 胜平负概率")
    st.json(prob)

    # ======================
    # 赔率
    # ======================
    odds = get_odds()

    st.subheader("💰 市场赔率")
    st.json(odds)

    # ======================
    # EV计算
    # ======================
    ev_results = calc_ev(prob, odds)

    st.subheader("📈 EV分析")
    st.json(ev_results)

    # ======================
    # 置信度 & 风险
    # ======================
    st.subheader("🧠 风险分析")

    risk_table = []
    for k in ev_results:
        risk_table.append({
            "market": k,
            "EV": ev_results[k]["EV"],
            "Kelly": kelly(prob[k], odds[k]),
            "Confidence": confidence_score(home, away)
        })

    st.json(risk_table)

    # ======================
    # 推荐榜单
    # ======================
    st.subheader("🔥 推荐排序")

    ranking = rank_bets(ev_results)

    st.json(ranking)
