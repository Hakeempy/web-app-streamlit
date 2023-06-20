# Imports 

import streamlit as st
import pandas as pd
import seaborn as sns

# 1. Title and Subheader
st.title('Data analysis')
st.subheader('Data Analysis using python and streamlit')

# 2. Upload Dataset
upload = st.file_uploader('Upload your Dataset(In CSV format)')
if upload is not None:
    data = pd.read_csv(upload)
    
# Show Dataset
if upload is not None:
    if st.checkbox('Preview Dataset'):
        if st.button('Head'):
            st.write(data.head())
        if st.button('Tail'):
            st.write(data.tail())

# Check Datatype of each column
if upload is not None:
    if st.checkbox('Datatype of Each column'):
        st.text('DataTypes')
        st.write(data.dtypes)
        
# Find the shape of our Dataset (The number of rows and columns)
if upload is not None:
    data_shape = st.radio("What dimension do you want to check?", ('Rows', 'Columns'))
    if data_shape == 'Rows':
        st.text('Number of Rows')
        st.write(data.shape[0])
    if data_shape == 'Columns':
        st.text('Number of columns')
        st.write(data.shape[1])
        
# Find null values in the DataSet
if upload is not None:
    test = data.isnull().values.any()
    if test == True:
        if st.checkbox('Null values in the DataSet'):
            sns.heatmap(data.isnull())
            st.pyplot()
            st.set_option('deprecation.showPyplotGlobalUse', False)
    else:
        st.success('Congratulations!! There are no missing values')
        
# Find duplicate values in the DataSet
if upload is not None:
    test = data.duplicated().any()
    if test == True:
        st.warning('This Dataset contains some duplicate values')
        dup = st.selectbox('Do you want to remove duplicate values?', ('Select one', 'Yes', 'No'))
        if dup == 'Yes':
            data = data.drop_duplicates()
            st.text('Duplicate values are removed')
        if  dup == 'No':
            st.text('Ok, no problem')
            
            
# Get overall statistics of the Dataset
if upload is not None:
    if st.checkbox('Summary of the Dataset'):
        st.write(data.describe(include = 'all'))
        
# About Section
if st.button('About App'):
    st.text('Built with streamlit')
    st.text('Thanks to streamlit')
    
# By 
if st.checkbox('By'):
    st.success('By Hakeem Wikireh')