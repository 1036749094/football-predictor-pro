import streamlit as st
from model import predict_match
from ev_engine import calc_ev
from betting import kelly_bet
from ranking import rank_bets

st.set_page_config(page_title="足球预测V25中文版")

st.title("⚽ 足球预测专家 V25 中文版")

home = st.text_input("主队")
away = st.text_input("客队")

if st.button("开始分析"):

    result = predict_match(home, away)

    st.subheader("📊 比赛预测结果")

    st.write("主队胜率：", result["home_win"])
    st.write("平局概率：", result["draw"])
    st.write("客队胜率：", result["away_win"])

    st.subheader("📈 EV分析")

    ev = calc_ev(result)
    st.write("EV评分：", ev)

    st.subheader("💰 资金管理建议")

    bet = kelly_bet(ev)
    st.write("建议投注比例：", bet)

    st.subheader("🔥 推荐榜单")

    rank = rank_bets(result)
    st.write(rank)
