import streamlit as st
import numpy as np
import pickle

# Load trained model
model = pickle.load(open('score_predictor_model.pkl', 'rb'))

# Title
st.title('Cricket Score Predictor')

# Inputs
batting_team = st.selectbox('Select Batting Team', ['Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab', 'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals', 'Royal Challengers Bangalore', 'Sunrisers Hyderabad'])
bowling_team = st.selectbox('Select Bowling Team', ['Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab', 'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals', 'Royal Challengers Bangalore', 'Sunrisers Hyderabad'])
overs = st.number_input('Overs Completed', min_value=5.0, max_value=20.0, step=0.1)
runs = st.number_input('Current Runs', min_value=0)
wickets = st.number_input('Wickets Fallen', min_value=0, max_value=10)
runs_in_prev_5 = st.number_input('Runs in Previous 5 Overs', min_value=0)
wickets_in_prev_5 = st.number_input('Wickets in Previous 5 Overs', min_value=0)

# Predict button
if st.button('Predict Final Score'):

    # Prepare input
    teams = ['Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab', 'Kolkata Knight Riders',
             'Mumbai Indians', 'Rajasthan Royals', 'Royal Challengers Bangalore', 'Sunrisers Hyderabad']

    temp_array = [1 if batting_team == team else 0 for team in teams] + \
                 [1 if bowling_team == team else 0 for team in teams] + \
                 [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]

    input_array = np.array([temp_array])

    # Predict
    prediction = int(model.predict(input_array)[0])

    st.success(f"Predicted Final Score Range: {prediction - 10} to {prediction + 5}")
