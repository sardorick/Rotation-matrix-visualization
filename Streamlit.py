import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


df = pd.read_csv("https://raw.githubusercontent.com/chriswmann/datasets/master/500_Person_Gender_Height_Weight_Index.csv")

st.title("BMI Visualization")
st.dataframe(df)
data_select = st.sidebar.selectbox("Select your Scatter Plot", ("BMI", "BMI For males", "BMI For females"))
menu = ["Original Vector", "Transformed Vector"]
rotation = st.sidebar.radio("Matrix", menu)
k = st.sidebar.slider("Choose your Rotation", 30, 100, 1)




def load_data(data_select):
# General scatter plot
       if data_select == "BMI":
           st.title("BMI")
           fig = px.scatter( df,  x='Weight', y='Height', title='BMI', color='Index')
                                

           st.plotly_chart(fig, use_column_width = True)


# Male BMI scatterplot

       elif data_select == "BMI For males":
            st.title("BMI For males")
            males = df.loc[(df['Gender'] == 'Male')]
            colorz = males.iloc[:, 3]
            fig = px.scatter(df.loc[(df['Gender'] == 'Male')],  x='Weight', y='Height', title='BMI For males', color=colorz)
            st.plotly_chart(fig, use_column_width = True)

#Female BMI scatter plot

       elif data_select == "BMI For Female":
            st.title("BMI For Female")
            males = df.loc[(df['Gender'] == 'Female')]
            colorz = males.iloc[:, 3]
            fig = px.scatter(df.loc[(df['Gender'] == 'Female')],  x='Weight', y='Height', title='BMI For females', color=colorz)
            st.plotly_chart(fig, use_column_width = True)


       else:
           print("no")

    
load_data(data_select)

# Males height

for_hist  = df.loc[(df['Gender'] == 'Male')]
heightss = for_hist.iloc[:, 1]
df_heights = heightss.to_frame()
fig, ax = plt.subplots()
ax.hist(df_heights, bins=20)

st.pyplot(fig)

fig = px.scatter(df['Weight'], df['Height'])
# fig = px.scatter(df['Weight'].mean(), df['Height'].mean())
st.plotly_chart(fig, use_column_width=True)
