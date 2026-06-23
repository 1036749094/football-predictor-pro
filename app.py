import streamlit as st
from model import predict_match

st.title("⚽ Football Predictor")

home = st.text_input("Home Team Name")
away = st.text_input("Away Team Name")

# 默认简单球队参数（防止报错）
default_team = {"attack": 1.2, "defense": 0.8}

if st.button("Predict"):
    result = predict_match(default_team, default_team)

    st.write(result)
