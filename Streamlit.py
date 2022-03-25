import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


df = pd.read_csv("https://raw.githubusercontent.com/chriswmann/datasets/master/500_Person_Gender_Height_Weight_Index.csv")

st.title("BMI Visualization")
st.dataframe(df)
# General scatter plot
fig = px.scatter( df,  x='Weight', y='Height', title='BMI', color='Index')
                                

st.plotly_chart(fig, use_column_width = True)

# Male BMI scatterplot
males = df.loc[(df['Gender'] == 'Male')]
colorz = males.iloc[:, 3]
fig = px.scatter(df.loc[(df['Gender'] == 'Male')],  x='Weight', y='Height', title='BMI For males', color=colorz)
st.plotly_chart(fig, use_column_width = True)

#Female BMI scatter plot
males = df.loc[(df['Gender'] == 'Female')]
colorz = males.iloc[:, 3]
fig = px.scatter(df.loc[(df['Gender'] == 'Female')],  x='Weight', y='Height', title='BMI For females', color=colorz)
st.plotly_chart(fig, use_column_width = True)

# Males height
for_hist  = df.loc[(df['Gender'] == 'Male')]
heightss = for_hist.iloc[:, 1]
df_heights = heightss.to_frame()
st.line_chart(df_heights)

fig = px.scatter(df['Weight'], df['Height'])
# fig = px.scatter(df['Weight'].mean(), df['Height'].mean())
st.plotly_chart(fig, use_column_width=True)
