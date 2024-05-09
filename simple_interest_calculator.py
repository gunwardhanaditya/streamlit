import streamlit as st

st.header("Simple Interest Calculator")

st.subheader("Principal Amount (Rs.)")
pa = st.number_input("Enter Principle Amount")

st.subheader("Annual Rate (%)")
ar = st.number_input("Enter Annual Rate")

st.subheader("Period Value (Year)")
pv = st.number_input("Enter Period Value")

simple_interest = (pa * ar * pv) / 100

total_value = pa + simple_interest

st.subheader("Simple Interest")
st.text(simple_interest)

st.subheader("Total Value (Principle Amount + Simple Interest)")
st.text(total_value)