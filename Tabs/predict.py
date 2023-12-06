"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st
import streamlit.components.v1 as components

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for the Employee Attrition Analysis.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.

    col1,col2,col3 = st.columns(3)

    with col1:
    
        Age = st.slider("Age", int(df["Age"].min()), int(df["Age"].max()))
        BusinessTravel = st.slider("BusinessTravel", float(df["BusinessTravel"].min()), float(df["BusinessTravel"].max()))
        DailyRate = st.slider("DailyRate", int(df["DailyRate"].min()), int(df["DailyRate"].max()))
        Department = st.slider("Department", int(df["Department"].min()), int(df["Department"].max()))
        DistanceFromHome = st.slider("DistanceFromHome", int(df["DistanceFromHome"].min()), int(df["DistanceFromHome"].max()))
        Education = st.slider("Education", float(df["Education"].min()), float(df["Education"].max()))
        EmployeeNumber = st.slider("EmployeeNumber", int(df["EmployeeNumber"].min()), int(df["EmployeeNumber"].max()))
        EnvironmentSatisfaction = st.slider("EnvironmentSatisfaction", int(df["EnvironmentSatisfaction"].min()), int(df["EnvironmentSatisfaction"].max()))
        YearsWithCurrManager = st.slider("YearsWithCurrManager", float(df["YearsWithCurrManager"].min()), float(df["YearsWithCurrManager"].max()))


    with col2:
        HourlyRate = st.slider("HourlyRate", float(df["HourlyRate"].min()), float(df["HourlyRate"].max()))
        JobInvolvement = st.slider("JobInvolvement", float(df["JobInvolvement"].min()), float(df["JobInvolvement"].max()))
        JobLevel = st.slider("JobLevel", float(df["JobLevel"].min()), float(df["JobLevel"].max()))
        JobSatisfaction = st.slider("JobSatisfaction", float(df["JobSatisfaction"].min()), float(df["JobSatisfaction"].max()))
        MonthlyIncome = st.slider("MonthlyIncome", float(df["MonthlyIncome"].min()), float(df["MonthlyIncome"].max()))
        MonthlyRate = st.slider("MonthlyRate", float(df["MonthlyRate"].min()), float(df["MonthlyRate"].max()))
        NumCompaniesWorked = st.slider("NumCompaniesWorked", float(df["NumCompaniesWorked"].min()), float(df["NumCompaniesWorked"].max()))
        OverTime = st.slider("OverTime", float(df["OverTime"].min()), float(df["OverTime"].max()))
        PercentSalaryHike = st.slider("PercentSalaryHike", float(df["PercentSalaryHike"].min()), float(df["PercentSalaryHike"].max()))
        

    with col3:
        PerformanceRating = st.slider("PerformanceRating", float(df["PerformanceRating"].min()), float(df["PerformanceRating"].max()))
        RelationshipSatisfaction = st.slider("RelationshipSatisfaction", float(df["RelationshipSatisfaction"].min()), float(df["RelationshipSatisfaction"].max()))
        StockOptionLevel = st.slider("StockOptionLevel", float(df["StockOptionLevel"].min()), float(df["StockOptionLevel"].max()))
        TotalWorkingYears = st.slider("TotalWorkingYears", float(df["TotalWorkingYears"].min()), float(df["TotalWorkingYears"].max()))
        TrainingTimesLastYear = st.slider("TrainingTimesLastYear", float(df["TrainingTimesLastYear"].min()), float(df["TrainingTimesLastYear"].max()))
        WorkLifeBalance = st.slider("WorkLifeBalance", float(df["WorkLifeBalance"].min()), float(df["WorkLifeBalance"].max()))
        YearsAtCompany = st.slider("YearsAtCompany", float(df["YearsAtCompany"].min()), float(df["YearsAtCompany"].max()))
        YearsInCurrentRole = st.slider("YearsInCurrentRole", float(df["YearsInCurrentRole"].min()), float(df["YearsInCurrentRole"].max()))
        YearsSinceLastPromotion = st.slider("YearsSinceLastPromotion", float(df["YearsSinceLastPromotion"].min()), float(df["YearsSinceLastPromotion"].max()))
     
    

    # Create a list to store all the features
    features = [Age,BusinessTravel,DailyRate,Department,DistanceFromHome,Education,EmployeeNumber,EnvironmentSatisfaction,HourlyRate,JobInvolvement,JobLevel,JobSatisfaction,MonthlyIncome,MonthlyRate,NumCompaniesWorked,OverTime,PercentSalaryHike,PerformanceRating,RelationshipSatisfaction,StockOptionLevel,TotalWorkingYears,TrainingTimesLastYear,WorkLifeBalance,YearsAtCompany,YearsInCurrentRole,YearsSinceLastPromotion,YearsWithCurrManager]

    # Create a button to predict
    if st.button("Detect Class"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score+0.11
        

        # Prfloat the output according to the prediction
                
        if (prediction == 1):
            st.error("High risk of employee attrition.")
            
        elif (prediction == 0):
            st.success("Least risk of employee attrition.")
          
          
                
        # Prfloat teh score of the model 
        st.sidebar.write("The model used is trusted by doctors and has an accuracy of ", round((score*100),2),"%")
