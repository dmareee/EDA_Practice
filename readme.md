# Bike Rentals System Analysis Dashboard
----
This project was created to fulfill the class submission Dicoding 'Belajar Analisis Data dengan Python'. It visualizes different factor that could have an impact on daily users count in bike rentals system such as season, weather, hour, temp. etc.
The implementation of this project goes through a general data analysis cycle from Data Wrangling, Data Cleaning, Exploratory Data Analysis, Data Visualization and Dashboard

## Project Cycle
----
1. Business Case (Questions):
    Before going in the data, needed to define analytical questions related to the data or problems need to solve
    Question :
    - In 24 Hours, When Does the Average User Rent A Bike?
    - Does the Weather Affect when users Rent Bikes?
    - How Many Users Uses Bike Rentals In 12 Months Range?
    - How Many Users Uses Bike Rentals on Weekdays Compared to Weekends?
    - How Many Users Uses Bike Rentals In 12 Months Range Based on User Type Category?

2. Data Wrangling :
    Starting from Gather Data, Assess Data, Clean Data. This phase is important as need to review the data if there's a few problems(outliers, missing value, duplicated values) that needed to be cleaned before dive in EDA.
    Few Problems founded in the assessing data :
    - Data Format on 'dteday' should be datetime format
    - Change labeling number to Categorical label on season, weathersit, workingday, holiday
    - Return the real value of temp, atemp, hum, windspeed

3. Exploratory Data Analysis (EDA)
    Exploring, digging through each features in dataset as we need base insight and answer analytic problems using descriptive analysis and data visualization to gather usage pattern, insights to answer the analytical problems

4. Data Visualization
    Results from EDA needed to be visualized applying various plots for presenting the insights founded in EDA phase.

5. Dashboard
    Final Presentation displaying the results using interactive analysis with streamlit 

## Content
----
1. Filtering date range and select multiple weather condition to visualized
2. Metrics User Count, Average Temperature, Weather, Average Humid
3. Visualization to answer each business case
4. Conclusion to whole analysis

# Setting Environment - Anaconda
'''
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
'''

# Setup Environment - Terminal
'''
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
'''

# Run Streamlit App
'''
streamlit run dashboard\dashboard.py
'''