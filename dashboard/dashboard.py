import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

rent_daily = pd.read_csv('dashboard/df_daily_cleaned.csv')
rent_hour = pd.read_csv('dashboard/df_hour_cleaned.csv')

rent_daily = rent_daily.rename(columns={
    'instant' : 'Record_id', 
    'dteday' : 'Date',
    'season' : 'Season',
    'yr' : 'Year',
    'mnth' : 'Month',
    'holiday' : 'Holiday',
    'weekday' : 'Weekdays',
    'workingday' : 'Workdays', 
    'weathersit': 'Weather',
    'temp' : 'Temperature',
    'atemp' : 'FeelsLike_Temp',
    'hum' : 'Humidity', 
    'windspeed' : 'Windspeed',
    'casual' : 'Casual_users',
    'registered' : 'Member_users',
    'cnt' : 'user_count'
})

rent_hour = rent_hour.rename(columns={
    'instant' : 'Record_id', 
    'dteday' : 'Date',
    'season' : 'Season',
    'yr' : 'Year',
    'mnth' : 'Month',
    'hr' : 'Hour',
    'holiday' : 'Holiday',
    'weekday' : 'Weekdays',
    'workingday' : 'Workdays', 
    'weathersit': 'Weather',
    'temp' : 'Temperature',
    'atemp' : 'FeelsLike_Temp',
    'hum' : 'Humidity', 
    'windspeed' : 'Windspeed',
    'casual' : 'Casual_users',
    'registered' : 'Member_users',
    'cnt' : 'user_count'
})

min_date = rent_daily['Date'].min()
max_date = rent_daily['Date'].max()
weather = rent_hour['Weather'].unique()


# Filter dataset based on the selected date range and weather conditions


st.title('Bike Rentals Dashboard')
st.subheader("Name : Damar Syarafi Ramadhan")

st.sidebar.title('Filters')
with st.sidebar:
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Date Range',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
    filter_weather = st.multiselect(
    label='Select Weather',
    options=(weather)
)

filtered_rent_daily = rent_daily[(rent_daily["Date"] >= str(min_date)) & 
                (rent_daily["Date"] <= str(max_date)) &
                (rent_daily['Weather'].isin(filter_weather))]

filtered_rent_hour = rent_hour[(rent_hour["Date"] >= str(min_date)) & 
                (rent_hour["Date"] <= str(max_date)) &
                (rent_hour['Weather'].isin(filter_weather))]

st.subheader("Dataset : Bike Rentals")
st.write(
    """
    Bike-sharing rental process is highly correlated to the environmental and seasonal settings. For instance, weather conditions, precipitation, day of week, season, hour of the day, etc. can affect the rental behaviors. The core data set is related to the two-year historical log corresponding to years 2011 and 2012 from Capital Bikeshare system, Washington D.C., USA which is 
    publicly available in http://capitalbikeshare.com/system-data. We aggregated the data on two hourly and daily basis and then  extracted and added the corresponding weather and seasonal information. Weather information are extracted from http://www.freemeteo.com. 
    """
)
    
tab1, tab2, tab3 = st.tabs(["Business Case", "Visualization", "Conclusion"])
with tab1:
    st.header('Defining Business Questions')
    st.markdown(
        """
        Question :
        - In 24 Hours, When Does the Average User Rent A Bike?
        - Does the Weather Affect when users Rent Bikes?
        - How Many Users Uses Bike Rentals In 12 Months Range?
        - How Many Users Uses Bike Rentals on Weekdays Compared to Weekends?
        - How Many Users Use Bike Rentals Services in 12 Months Based on User Type Category?"""
    )
    

with tab2:
    st.header('Visualization & Data Explanatory')
    st.subheader(f'Metrics Count {str(min_date), str(max_date)}')
    total_user = filtered_rent_daily['user_count'].sum()
    temp_avg = filtered_rent_daily['Temperature'].mean()
    hum_avg = filtered_rent_daily['Humidity'].mean()
    col1, col2= st.columns(2)
 
    with col1:
        st.metric("user_count", value=int(total_user))
        st.metric('Weather', value=str(filter_weather))
    with col2:
        st.metric("Average Temperature (C)", value=round(temp_avg, 2))
        st.metric('Average Humidity', value=round(hum_avg, 2))
        
    # Question 1 Vis
    st.subheader('Question 1 : In 24 Hours, When Does the Average User Rent A Bike?')
    hourly_user = filtered_rent_hour.groupby(by='Hour')['user_count'].mean().reset_index()
    # hourly_user
    st.line_chart(hourly_user, x='Hour', y='user_count', color='#a84832')
    
    # Question 2 Vis
    st.subheader('Question 2 : How Much Average of Temp & Humid by Season?')
    seasonth = filtered_rent_daily.groupby(by='Season').agg({
    'Temperature' : 'mean',
    'Humidity' : 'mean'}).reset_index()
    seasonth
    col1, col2= st.columns(2)
    with col1:
            st.bar_chart(seasonth, x='Season', y='Temperature', color='#f9ab3c')
    with col2:
        st.bar_chart(seasonth, x='Season', y='Humidity', color='#fc272f')
    
    # Question 3 Vis
    st.subheader('Question 3 : How Many Users Uses Bike Rentals In Season?')
    seasonby = filtered_rent_daily.groupby(by='Season').user_count.mean()
    st.write('Seasonby : Users')
    col1, col2 = st.columns(2)
    with col1:
        st.bar_chart(data=seasonby, color='#f31e68')
    with col2:
        seasonby
        
    # Question 4 Vis
    st.subheader('Question 4 : How Many Users Uses Bike Rentals on Weekdays Compared to Weekends?')
    workingby = filtered_rent_daily.groupby(by='Workdays').user_count.mean().reset_index()
    daily_user = rent_daily.groupby(by='Weekdays').user_count.mean().reset_index()
    st.bar_chart(workingby, x='Workdays', y='user_count', color='#f31e68')
    st.line_chart(daily_user, x='Weekdays', y='user_count', color='#f31e68')
    
    # Question 5 Advanced Analysis
    st.subheader('User Group Clustering : How Many Use Bike Rentals Services in 12 Months Based on User Type Category?')
    monthly_category_user = rent_daily.groupby(['Casual_users', 'Member_users']).Month.mean().reset_index()
    st.bar_chart(monthly_category_user, x='Month', stack=False, color=['#f9ab3c',  '#f31e68'])
    
with tab3:
    st.markdown(
        """
        ## Conclusion
        - Conclusion Question 1 : Peak Hours happened at 8.am and 5 p.m, which means in everyday users tend to use bike rentals to go to work in the morning (8 a.m) and go back from work (5 p.m) as their main choice of transportation going pass through city traffic.+ Conclusion Question 1 : 
    - Peak Hours happened at 8.am and 5 p.m, which means in everyday users tend to use bike rentals to go to work in the morning (8 a.m) and go back from work (5 p.m) as their main choice of transportation going pass through city traffic.
    - Meanwhile decreasing trend show inactive hour as there no productive activities from 9pm till 5am

    + Conclusion Question 2 : 
        - The Highest Average Temperature which is on Fall with a value of averaging 28.9 Celcius, meanwhile the Highest Humid is on Winter averaging 66.8%
        - From this insight, temperature increases, warmer air can hold more water vapor. For example, at 20°C (68°F), air can hold twice as much water vapor as it can at 28°C. If the amount of water vapor in the air stays the same, the relative humidity decreases. Conversely high humidity created more cooler/chilled temperature cause of the amount of low water vapor in air from the low temperature.

    + Conclusion Question 3 : 
        - Users tend to cycle during fall season, supported by user counts have the highest number bike rentals in fall season.
        - From earlier question, during fall season has more users than other season, season fall has both relative high average temperature and humidity (temp=28 C, hum=63%) with clear weather, Fall strikes a balance: warm enough to avoid cold discomfort but cool enough to prevent heat stress, with minimal rain disruption.

    + Conclusion Question 4 : 
        - Users tend to chose Bike Rentals as their mode of transportation cycling through city traffic every working day from Monday - Friday and had a peak count of users in Friday.

    + Conclusion Question 5 (Advanced) : 
        - The number of registered users who use the rental system on weekdays is greater, so they prioritize practical use to avoid traffic jams on weekdays or the distance to the workplace which is close.
        - Meanwhile, regular users tend to use bicycle rentals for recreational purposes on holidays.

    After Exploring the data, this concludes that User Rent bikes as their main choice of transportation to go to work in the morning and go back from work in the evening, additional fact they chose rental bike is clear/cloudy weather as they enjoy the fall season is a great season for riding bikes. (https://transportation.ucla.edu/blog/why-fall-best-season-bike-riding)

    + Recommended act after this analysis is :
        - Charge premium rates during peak hours on weekdays (around 8am & 9am)
        - Marketing campaign to casual users with weekend promo discounts and holidays occasions example : valentine couple ride discount, family ride discount, package with recreational parks tickets, etc.
    """
    )