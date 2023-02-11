
import streamlit as st
import pickle  
import numpy as np
st.set_page_config(layout="wide", page_icon='👶', page_title="Fetal Health")
with open("style.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

def load_model():
    with open('Predict_model.pkl', 'rb') as file:
        data = pickle.load(file)  
        rfst_loaded=data["model"]  
    return rfst_loaded

Mode=load_model()

def show_predict_page():
    st.title("""Fetal health recognition👶""")
    st.write("""We need some information to recognize how health the baby is""")
    st.write("""So please fill this form""")

    #baseline_value
    baseline_value=st.number_input("baseline value",step=1.,format="%.6f")
    st.write('The current number is ', baseline_value)

    #accelerations
    accelerations=st.number_input("accelerations",step=1.,format="%.6f")
    st.write('The current number is ', accelerations)

    #fetal_movement
    fetal_movement=st.number_input("fetal_movement",step=1.,format="%.6f")
    st.write('The current number is ', fetal_movement)

    #uterine_contractions
    uterine_contractions=st.number_input("uterine_contractions",step=1.,format="%.6f")
    st.write('The current number is ', uterine_contractions)

    #light_decelerations
    light_decelerations=st.number_input("light_decelerations",step=1.,format="%.6f")
    st.write('The current number is ', light_decelerations)

    #severe_decelerations
    severe_decelerations=st.number_input("severe_decelerations",step=1.,format="%.6f")
    st.write('The current number is ', severe_decelerations)

    #prolongued_decelerations
    prolongued_decelerations=st.number_input("prolongued_decelerations",step=1.,format="%.6f")
    st.write('The current number is ', prolongued_decelerations)

    #abnormal_short_term_variability
    abnormal_short_term_variability=st.number_input("abnormal_short_term_variability",step=1.,format="%.6f")
    st.write('The current number is ', abnormal_short_term_variability)

    #mean_value_of_short_term_variability
    mean_value_of_short_term_variability=st.number_input("mean_value_of_short_term_variability",step=1.,format="%.6f")
    st.write('The current number is ', mean_value_of_short_term_variability)

    #percentage_of_time_with_abnormal_long_term_variability
    percentage_of_time_with_abnormal_long_term_variability=st.number_input("percentage_of_time_with_abnormal_long_term_variability",step=1.,format="%.6f")
    st.write('The current number is ', percentage_of_time_with_abnormal_long_term_variability)  

    #mean_value_of_long_term_variability     
    mean_value_of_long_term_variability=st.number_input("mean_value_of_long_term_variability",step=1.,format="%.6f")
    st.write('The current number is ', mean_value_of_long_term_variability)

    #histogram_width
    histogram_width=st.number_input("histogram_width",step=1.,format="%.6f")
    st.write('The current number is ', histogram_width)

    #histogram_min   
    histogram_min=st.number_input("histogram_min",step=1.,format="%.6f")
    st.write('The current number is ', histogram_min)

    #histogram_max
    histogram_max=st.number_input("histogram_max",step=1.,format="%.6f")
    st.write('The current number is ', histogram_max)

    #histogram_number_of_peaks
    histogram_number_of_peaks=st.number_input("histogram_number_of_peaks",step=1.,format="%.6f")
    st.write('The current number is ', histogram_number_of_peaks)

    #histogram_number_of_zeroes
    histogram_number_of_zeroes=st.number_input("histogram_number_of_zeroes",step=1.,format="%.6f")
    st.write('The current number is ', histogram_number_of_zeroes)

    #histogram_mode
    histogram_mode=st.number_input("histogram_mode",step=1.,format="%.6f")
    st.write('The current number is ', histogram_mode)
    
    #histogram_mean
    histogram_mean=st.number_input("histogram_mean",step=1.,format="%.6f")
    st.write('The current number is ', histogram_mean)

    #histogram_median
    histogram_median=st.number_input("histogram_median",step=1.,format="%.6f")
    st.write('The current number is ', histogram_median)
 
    #histogram_variance
    histogram_variance=st.number_input("histogram_variance",step=1.,format="%.6f")
    st.write('The current number is ', histogram_variance)

    #histogram_variance
    histogram_tendency=st.number_input("histogram_tendency",step=1.,format="%.6f")
    st.write('The current number is ', histogram_tendency)


    ok=st.button("Predict")
    if ok:
        X=[[baseline_value,accelerations,fetal_movement,uterine_contractions,light_decelerations,severe_decelerations,prolongued_decelerations,abnormal_short_term_variability,mean_value_of_short_term_variability,percentage_of_time_with_abnormal_long_term_variability,mean_value_of_long_term_variability,histogram_width,histogram_min,histogram_max,histogram_number_of_peaks,histogram_number_of_zeroes,histogram_mode,histogram_mean,histogram_median,histogram_variance,histogram_variance]]
        # _loaded = data["model"]
        Prediction=Mode.predict(X)
        if Prediction[0]==1.0:
            st.subheader(f"Normal")
        elif Prediction[0]==2.0:
            st.subheader(f"Suspect")
        elif Prediction[0]==3.0:
            st.subheader(f"Pathological")
       

        st.subheader(f"Prediction of the fetal movement is {Prediction[0]}")