import streamlit as st
import pandas as pd
import numpy as np

st.title("Labor Forecasting Tool")

st.header("Input Flight Data")
passenger_volume = st.number_input("Projected Passenger Volume", min_value=0, value=1000)
flight_schedules = st.number_input("Number of Flights", min_value=0, value=10)

staffing_multiplier = 0.1  #Ex: 10% of passenger volume
labor_requirements = passenger_volume * staffing_multiplier + flight_schedules * 5

st.subheader("Forecasted Labor Requirements")
st.write(f"Projected Staffing Needs: {labor_requirements} employees")

st.header("Variance Analysis")
actual_labor = st.number_input("Actual Labor Used", min_value=0, value=int(labor_requirements))
variance = actual_labor - labor_requirements
st.write(f"Variance: {variance} employees")

st.header("Downloadable Report")
data = {
    'Passenger Volume': [passenger_volume],
    'Flight Schedules': [flight_schedules],
    'Forecasted Labor': [labor_requirements],
    'Actual Labor': [actual_labor],
    'Variance': [variance]
}
df = pd.DataFrame(data)
st.write(df)
st.download_button(
    label="Download Report as CSV",
    data=df.to_csv(index=False),
    file_name='labor_forecast_report.csv',
    mime='text/csv'
)