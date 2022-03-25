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
st.title('Histogram of males height')
for_hist  = df.loc[(df['Gender'] == 'Male')]
heightss = for_hist.iloc[:, 1]
df_heights = heightss.to_frame()
fig, ax = plt.subplots()
ax.hist(df_heights, bins=20)

st.pyplot(fig)


# Males weight
st.title('Histogram of males weight')
for_hist  = df.loc[(df['Gender'] == 'Male')]
weightss = for_hist.iloc[:, 2]
df_weights = weightss.to_frame()
fig, ax = plt.subplots()
ax.hist(df_weights, bins=20)

st.pyplot(fig)

# Female height
st.title('Histogram of female height')
for_hist  = df.loc[(df['Gender'] == 'Female')]
heightss = for_hist.iloc[:, 1]
df_heights = heightss.to_frame()
fig, ax = plt.subplots()
ax.hist(df_heights, bins=20)

st.pyplot(fig)

# Female weight
fig, ax = plt.subplots(figsize=(8,8))
st.title('Histogram of females weight')
for_hist  = df.loc[(df['Gender'] == 'Female')]
weightss = for_hist.iloc[:, 2]
df_weights = weightss.to_frame()
fig, ax = plt.subplots()
ax.hist(df_weights, bins=20)
st.pyplot(fig)

# Plot mean of Weight and heigh
mean_vector = [df.Weight.mean(), df.Height.mean()]
fig1 = px.scatter(df['Weight'], df['Height'])
# mean_height = df['Weight'].mean()
# mean_weight = df['Height'].mean()
fig = px.scatter(mean_vector)
st.plotly_chart(fig1, use_column_width=True)

## this needs rework


### Mean per BMI
df2 = df.groupby('Index').mean()
fig = px.scatter(df2,  x='Weight', y='Height', title='Mean per BMI', color=('Extremely weak mean', 'Weak', 'Normal', 'Overweight', 'Obesity', 'Extreme Obesity'))
fig.update_traces(marker=dict(size=16))
st.plotly_chart(fig, use_column_width = True)
