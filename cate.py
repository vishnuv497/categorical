import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit App
st.title("Categorical Analytics Dashboard")

# File Upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Dataset Preview:")
    st.dataframe(df.head())
    
    # Select Categorical Column
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns.tolist()
    if not categorical_columns:
        st.warning("No categorical columns found in the dataset.")
    else:
        selected_column = st.selectbox("Select a categorical column to analyze", categorical_columns)
        
        if selected_column:
            st.subheader(f"Distribution of {selected_column}")
            value_counts = df[selected_column].value_counts()
            
            # Bar Chart
            fig, ax = plt.subplots()
            value_counts.plot(kind='bar', ax=ax, color='skyblue')
            ax.set_xlabel(selected_column)
            ax.set_ylabel("Count")
            ax.set_title(f"Bar Chart of {selected_column}")
            st.pyplot(fig)
            
            # Pie Chart
            fig, ax = plt.subplots()
            value_counts.plot(kind='pie', ax=ax, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
            ax.set_ylabel("")
            ax.set_title(f"Pie Chart of {selected_column}")
            st.pyplot(fig)
