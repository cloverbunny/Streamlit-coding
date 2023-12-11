import streamlit as st 
#import openai
#from openai import OpenAI 

st.write('Welcome to a BMI calculator! ')

def calculate_bmi(weight, height):
    bmi = (weight/height**2)*703
    return bmi 

weight = st.number_input('Insert weight (lbs)',value=90,)
st.write('Your weight in lbs is ', weight)

height = st.number_input('Insert height (inches)',value=60)
st.write('Your height in inches is ', height)

if st.button('Click here to calculate BMI'):
    bmi = calculate_bmi(weight,height)
    st.write('Your BMI is ', bmi)
    if bmi<18.5:
        st.write('You are underweight.')
    elif (bmi>18.5) and (bmi<25):
        st.write('You are a normal weight.')
    elif bmi>25 and bmi<30:
        st.write('You are overweight.')
    else:
        st.write('You are obese.')


st.write('''
         BMI guidelines: \n  
         If your BMI is less than 18.5, it falls within the underweight range. \n  
         If your BMI is 18.5 to <25, it falls within the healthy weight range. \n  
         If your BMI is 25.0 to <30, it falls within the overweight range. \n  
         If your BMI is 30.0 or higher, it falls within the obesity range.
         ''')


