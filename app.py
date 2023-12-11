import streamlit as st

st.title("Find largest of three numbers")

st.header("Enter your inputs ")

num1 = st.number_input('Input the first number')
num2 = st.number_input('Input the second number')
num3 = st.number_input('Input the third number')

def maximum():
    lis = [num1 , num2 , num3]
    a = max(lis)
    st.success(f"Largest = {a}")

if st.button("Calculate result"):
    maximum()
