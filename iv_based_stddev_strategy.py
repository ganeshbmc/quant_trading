import streamlit as st

st.write("""
# Simple strategy based on ATM IV and std deviations

This app asks for the following details from you:

    > Name of the Underlying
    > Spot price
    > Number of days till expiry
    > ATM IV

Based on these inputs, it returns a table which contains the breakeven points for each predefined standard deviation.
""")

#Get Input

st.header('Input Parameters')


underlying = st.text_input('Enter the name of the underlying')
spot_prev_close = st.number_input('Enter spot price of interest')
days_to_expiry = st.number_input('Enter the number of days to expiry')
atm_iv = st.number_input('Enter the ATM IV value of the underlying')
    

data = {'Underlying_name': underlying,
        'Spot_price': spot_prev_close,
        'Number_of_days_to_expiry': days_to_expiry,
        'ATM_IV': atm_iv
        }


st.subheader('User input parameters')
st.write(data)

# App engine

result = data['Number_of_days_to_expiry'] * data['ATM_IV']

#Output

st.subheader('Result of calculation is:')
st.write(data['Underlying_name'])
st.write(result)