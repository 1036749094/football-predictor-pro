import streamlit as st
import numpy as np
from math import exp

st.set_page_config(page_title="Football Predictor V17", layout="wide")

st.title("⚽ Football Predictor V17 Online")

st.sidebar.header("Match Input")

base = st.sidebar.slider("Base Goal",1.0,2.0,1.3)
attack = st.sidebar.slider("Attack",0.5,2.0,1.4)
defense = st.sidebar.slider("Defense",0.5,2.0,1.1)
elo = st.sidebar.slider("Elo Diff",-300,300,50)
finish = st.sidebar.slider("Finish",0.5,2.0,1.1)
form = st.sidebar.slider("Form",0.5,2.0,1.0)
health = st.sidebar.slider("Health",0.5,1.2,1.0)
motivation = st.sidebar.slider("Motivation",0.8,1.3,1.0)

def lam(b,a,d,e,f,fo,h,m):
    return b*a*d*exp(e/600)*f*fo*h*m

lh = lam(base,attack,defense,elo,finish,form,health,motivation)
la = lam(base,1.2,1.0,-elo,0.95,1.0,1.0,1.0)

st.subheader("Expected Goals (λ)")
st.write("Home:", round(lh,3))
st.write("Away:", round(la,3))

n = 100000
hg = np.random.poisson(lh,n)
ag = np.random.poisson(la,n)

home = np.mean(hg > ag)
draw = np.mean(hg == ag)
away = np.mean(hg < ag)

st.subheader("Probabilities")

col1, col2, col3 = st.columns(3)
col1.metric("Home Win", f"{home:.2%}")
col2.metric("Draw", f"{draw:.2%}")
col3.metric("Away Win", f"{away:.2%}")

st.subheader("Market Insight")
st.write("BTTS:", np.mean((hg>0)&(ag>0)))
st.write("Over 2.5:", np.mean((hg+ag)>=3))
