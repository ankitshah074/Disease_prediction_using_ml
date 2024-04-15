# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 00:15:44 2024

@author: ankit
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))


with st.sidebar:
    
    selected = option_menu('Disease prediction system',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction'],
                           default_index = 0)
    
    
if(selected  =='Diabetes Prediction'):    
    st.title('Diabetes Prediction')
    

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
       
        Glucose = st.text_input('Glucose Level')
    



    with col3:
        
        BloodPressure = st.text_input('BloodPressure value')

    
    with col1:
       
        SkinThickness = st.text_input('Skin Thickness value')

    
    with col2:
       
        Insulin = st.text_input('Insulin Level')

    
    with col3:
        
        BMI = st.text_input('BMI value')

    
    with col1:
       
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

   
    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    
diab_diagnosis = ''

    # creating a button for Prediction

    
if st.button('Diabetes Test Result'):
    
    user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

    user_input = [float(x) for x in user_input]

    diab_prediction = diabetes_model.predict([user_input])

    if diab_prediction[0] == 1:
        
            diab_diagnosis = 'The Person is tested Positive for Diabetes'
    else:
            diab_diagnosis = 'The Person is tested Negative for Diabetes'

    st.success(diab_diagnosis)    

if selected  == 'Heart Disease Prediction':  
        
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)    
