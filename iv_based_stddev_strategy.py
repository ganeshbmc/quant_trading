import streamlit as st
import math as m
import numpy as np
import pandas as pd
import datetime as dt

st.write("""
# Calculate breakeven points based on ATM IV, time to expiry and std deviations!

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
spot_prev_close = st.number_input('Enter spot price of interest', step=0.1)
days_to_expiry = st.number_input('Enter the number of days to expiry', step=0.5)
atm_iv = st.number_input('Enter the ATM IV value of the underlying',step=0.1)
    

# data = {'Underlying_name': underlying,
#         'Spot_price': spot_prev_close,
#         'Number_of_days_to_expiry': days_to_expiry,
#         'ATM_IV': atm_iv
#         }


# st.subheader('User input parameters')
# st.write(data)


# App engine

# result = data['Number_of_days_to_expiry'] * data['ATM_IV']

def expected_move_pct(atm_iv, days_to_expiry, risk_stddev):
    exp_move_pct = (atm_iv/(m.sqrt(256/days_to_expiry)))
    exp_move_pct_for_desired_risk = exp_move_pct * risk_stddev
    return exp_move_pct, exp_move_pct_for_desired_risk

def get_strikes(underlying, atm_iv, spot_prev_close, days_to_expiry):

    heads = ["Percentage move", "Points to move from spot", "Lower strike", "Upper strike"]
    df = pd.DataFrame(index=heads)

    std_devs = [0.75, 1, 1.25, 1.5, 1.75, 2, 2.5]
    for risk_stddev in std_devs:
        mv1, mv2 = expected_move_pct(atm_iv, days_to_expiry, risk_stddev)
        points_move = spot_prev_close * (mv2/100)
        lower_strike = spot_prev_close - points_move
        upper_strike = spot_prev_close + points_move

        temp = [f"{round(mv2, 2)}%", 
                f"{int(points_move)}", f"{int(lower_strike)}", f"{int(upper_strike)}"]
        df[f"{risk_stddev} SD"] = temp

    # statement = f"Underlying: {underlying.upper()}\nSpot price of interest: {spot_prev_close}\nPeriod of interest: {days_to_expiry}\nATM IV: {atm_iv}\n\n"
    # print(statement)
    return df

result = get_strikes(underlying, atm_iv, spot_prev_close, days_to_expiry)

#Output

st.subheader("Here's your Output!")
# st.write()
st.dataframe(result)