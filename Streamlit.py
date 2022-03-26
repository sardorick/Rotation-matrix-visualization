import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


df = pd.read_csv("https://raw.githubusercontent.com/chriswmann/datasets/master/500_Person_Gender_Height_Weight_Index.csv")


data_select = st.sidebar.selectbox("Select the data you want to see", ("Data overview", "BMI scatterplots", "Histogram data for wieghts in different categories"))
# hist_select = st.sidebar.selectbox("Choose which histogram you want", ("Male height", "Male weight", "Female height", "Female weight"))


rotation = st.sidebar.checkbox("Original Vector")


# if rotation == "Original Vector":
#     st.title("Original Vector") 
#     y, x = np.indices((5, 4))
#     y = y.flatten()
#     x = x.flatten()
#     xy = np.row_stack((x, y))
#     fig = px.scatter(xy, x='X axis', y='Y axis', title="Original Vector")
#     st.plotly_chart(fig, use_column_width = True)

# rotation1 = st.sidebar.checkbox("Transformed Vector")
# deg = st.sidebar.slider("Choose your Rotation", 30, 100, 1)    

# def rot_mat(deg):
#     if rotation1 == "Transformed Vector":
#         st.title("Transformed Vector")
#         theta = deg/180*np.pi
#         cos = np.cos(theta)
#         sin = np.sin(theta)
#     return np.array([[cos, -sin], [sin, cos]])

# r = rot_mat(deg)
# rxy = r@xy
# fig = px.scatter(rxy, x='X axis', y='Y axis', title="Transformed Vector")
# st.plotly_chart(fig, use_column_width = True)

    

def load_data(data_select):
        # General scatter plot
        if data_select == "BMI scatterplots":
            st.title("BMI")
            fig = px.scatter( df,  x='Weight', y='Height', title='BMI', color='Index')
            st.plotly_chart(fig, use_column_width = True)
            # Male BMI scatterplot
            st.title("BMI For males")
            males = df.loc[(df['Gender'] == 'Male')]
            colorz = males.iloc[:, 3]
            fig = px.scatter(df.loc[(df['Gender'] == 'Male')],  x='Weight', y='Height', title='BMI For males', color=colorz)
            st.plotly_chart(fig, use_column_width = True)

            #Female BMI scatter plot

            st.title("BMI For Female")
            females = df.loc[(df['Gender'] == 'Female')]
            colorz = females.iloc[:, 3]
            fig1 = px.scatter(df.loc[(df['Gender'] == 'Female')],  x='Weight', y='Height', title='BMI For females', color=colorz)
            st.plotly_chart(fig1, use_column_width = True)
        
        elif data_select == "Histogram data for wieghts in different categories":
            # Males height
            st.title('Histogram of males height')
            for_hist  = df.loc[(df['Gender'] == 'Male')]
            heightss = for_hist.iloc[:, 1]
            df_heights = heightss.to_frame()
            fig, ax = plt.subplots()
            ax.hist(df_heights, bins=20)
            plt.xlabel('Weight, kg')
            plt.ylabel('Frequency')
            st.pyplot(fig)


            # Males weight
            st.title('Histogram of males weight')
            for_hist  = df.loc[(df['Gender'] == 'Male')]
            weightss = for_hist.iloc[:, 2]
            df_weights = weightss.to_frame()
            fig, ax = plt.subplots()
            ax.hist(df_weights, bins=20)
            plt.xlabel('Weight, kg')
            plt.ylabel('Frequency')
            st.pyplot(fig)

            # Female height
            st.title('Histogram of female height')
            for_hist  = df.loc[(df['Gender'] == 'Female')]
            heightss = for_hist.iloc[:, 1]
            df_heights = heightss.to_frame()
            fig, ax = plt.subplots()
            ax.hist(df_heights, bins=20)
            plt.xlabel('Weight, kg')
            plt.ylabel('Frequency')
            st.pyplot(fig)

        # Female weight
            fig, ax = plt.subplots(figsize=(8,8))
            st.title('Histogram of females weight')
            for_hist  = df.loc[(df['Gender'] == 'Female')]
            weightss = for_hist.iloc[:, 2]
            df_weights = weightss.to_frame()
            fig, ax = plt.subplots()
            ax.hist(df_weights, bins=20)
            plt.xlabel('Weight, kg')
            plt.ylabel('Frequency')
            st.pyplot(fig)
        elif data_select == "Data overview":
            st.title("BMI Visualization")
            st.dataframe(df)
        else:
            print("no")

    
load_data(data_select)



# Plot mean of Weight and heigh
agree = st.sidebar.checkbox('Mean')
if agree:
    mean_vector = [df.Weight.mean(), df.Height.mean()]
    fig1 = px.scatter(df['Weight'], df['Height'])
    # mean_height = df['Weight'].mean()
    # mean_weight = df['Height'].mean()
    fig = px.scatter(mean_vector)
    st.plotly_chart(fig1, use_column_width=True)

## this needs rework

agree1 = st.sidebar.checkbox('Mean per BMI')
if agree1:
### Mean per BMI
        df2 = df.groupby('Index').mean()
        fig = px.scatter(df2,  x='Weight', y='Height', title='Mean per BMI', color=('Extremely weak mean', 'Weak', 'Normal', 'Overweight', 'Obesity', 'Extreme Obesity'))
        fig.update_traces(marker=dict(size=16))
        st.plotly_chart(fig, use_column_width = True)


