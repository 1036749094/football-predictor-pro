import streamlit as st
import numpy as np
from math import exp
from betting import ev, kelly, recommendation
from odds import get_odds

st.set_page_config(page_title="V18 足球量化交易系统", layout="wide")

st.title("⚽ 足球量化交易系统 V18（专业版）")

# ---------------- 输入区 ----------------
st.sidebar.header("📊 比赛参数（模型输入）")

base = st.sidebar.slider("联赛平均进球",1.0,2.0,1.3)
attack = st.sidebar.slider("进攻能力",0.5,2.0,1.4)
defense = st.sidebar.slider("防守能力",0.5,2.0,1.1)
elo = st.sidebar.slider("Elo实力差", -300,300,50)
finish = st.sidebar.slider("射门效率",0.5,2.0,1.1)
form = st.sidebar.slider("近期状态",0.5,2.0,1.0)
health = st.sidebar.slider("阵容健康",0.5,1.2,1.0)
motivation = st.sidebar.slider("比赛动机",0.8,1.3,1.0)

def lam(b,a,d,e,f,fo,h,m):
    return b*a*d*exp(e/600)*f*fo*h*m

lh = lam(base,attack,defense,elo,finish,form,health,motivation)
la = lam(base,1.2,1.0,-elo,0.95,1.0,1.0,1.0)

st.subheader("⚽ 预期进球（xG）")
st.write("主队：", round(lh,3))
st.write("客队：", round(la,3))

# ---------------- 模拟 ----------------
n = 100000
hg = np.random.poisson(lh,n)
ag = np.random.poisson(la,n)

p_home = np.mean(hg > ag)
p_draw = np.mean(hg == ag)
p_away = np.mean(hg < ag)

st.subheader("📊 胜平负概率")
col1,col2,col3 = st.columns(3)

col1.metric("主胜", f"{p_home:.2%}")
col2.metric("平局", f"{p_draw:.2%}")
col3.metric("客胜", f"{p_away:.2%}")

# ---------------- 赔率 ----------------
st.subheader("💰 真实赔率（可手动/接口）")

odds = get_odds()

h_odds = st.number_input("主胜赔率", value=odds["home"])
d_odds = st.number_input("平局赔率", value=odds["draw"])
a_odds = st.number_input("客胜赔率", value=odds["away"])

# ---------------- EV分析 ----------------
st.subheader("📈 投注价值分析（EV + Kelly）")

home_r = recommendation(p_home, h_odds)
draw_r = recommendation(p_draw, d_odds)
away_r = recommendation(p_away, a_odds)

st.json({
    "主胜": home_r,
    "平局": draw_r,
    "客胜": away_r
})

# ---------------- 推荐 ----------------
best = max([
    ("主胜", home_r["EV"]),
    ("平局", draw_r["EV"]),
    ("客胜", away_r["EV"])
], key=lambda x: x[1])

st.subheader("🔥 最优投注建议")
st.success(f"推荐选择：{best[0]}（EV最高）")
