import streamlit as st 
#import openai

from openai import OpenAI 

st.write('Hello world')

def calculate_bmi(weight, height):
    bmi = (weight/height**2)*703
    return bmi 

weight = st.number_input('Insert weight (lbs)',value=90,)
st.write('The current number in lbs is ', weight)

height = st.number_input('Insert height (inches)',value=60)
st.write('The height in inches is ', height)

if st.button('Click here to calculate BMI'):
    bmi = calculate_bmi(weight,height)
    st.write('The BMI is ', bmi)
    if bmi<18.5:
        st.write('You are underweight')
    elif bmi>18.5 & bmi<25:
        st.write('You are a normal weight')


