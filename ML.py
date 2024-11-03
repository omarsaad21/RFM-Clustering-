import streamlit as st 
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
import plotly.graph_objects as go


# Title of the ML page
st.title("Machine Learning Part")



st.markdown("""
### Summary:
In this section, we will implement a customer segmentation model to recommend the best merchants for each user as targeted offers.
The model will leverage various clustering algorithms to group users based on their transaction behaviors and preferences.
""")



# Define a function to display model accuracies
def show_model_accuracies():
    # Example accuracies (replace with actual model accuracy results)
    accuracies = {
        "K means": "Solhoutte score for k:means: 0.784,Davies-Bouldin Index: 0.614",
        
    }
    
    st.write("### classification algorithm outcome")
    for model, accuracy in accuracies.items():
        st.write(f"{model}: {accuracy}")

# Button to show model accuracies
if st.button("Show algorithm outcome"):
    show_model_accuracies()