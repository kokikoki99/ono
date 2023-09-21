import streamlit as st
import random

if st.title('おみくじアプリ')
results=["大吉","忠吉","小吉","吉","凶","大凶"]
result=random.choice(results)
st.write(f"結果:{result}"