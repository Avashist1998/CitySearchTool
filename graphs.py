# imports
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import time
import multiprocessing
import plotly.graph_objects as go
import plotly.express as px
import seaborn as sns
import plotly.figure_factory as ff


#Paths to all the data files
data_path = os.path.join(os.getcwd(),"data")
pop_path = os.path.join(data_path,"City_based_population.csv")
income_path = os.path.join(data_path,"kaggle_income.csv")
div_path = os.path.join(data_path,"population.csv")

st.title("Funky Graphs, Let's get it")

#table
Income_df = pd.read_csv(income_path,encoding = 'latin-1')
st.line_chart(Income_df[['Mean']])

st.write("Data Table Attempt #1:")

# Lady's weird plot 

z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')
z = z_data.values
sh_0, sh_1 = z.shape
x, y = np.linspace(0, 1, sh_0), np.linspace(0, 1, sh_1)
fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
fig.update_layout(title='IRR', autosize=False,
                  width=800, height=800,
                  margin=dict(l=40, r=40, b=40, t=40))
st.plotly_chart(fig)


## TWO DIFF WAYS TO PLOT PIE CHARTS ##

# Pie Chart with plotly.express
df = px.data.tips()
fig = px.pie(df, values='tip', names='day')
st.plotly_chart(fig)

# Pie Chart with plotly.graph_objects

import plotly.graph_objects as go

labels = ['American Indian','White','Asian','Black','Pacific Islander','Two or more races','Unknown']
values = [4500, 2500, 1053, 500,455,788,670]

fig_2 = go.Figure(data=[go.Pie(labels=labels, values=values)])
st.plotly_chart(fig_2)


st.set_option('deprecation.showPyplotGlobalUse', False)

# Seaborn Line Plot 
df = pd.DataFrame({'x': [1, 2, 3], 'y': [10, 30, 70]})
sns.lineplot(x='x', y='y', data=df)
st.pyplot()




# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2
# Group data together
hist_data = [x1, x2, x3]
group_labels = ['Group 1', 'Group 2', 'Group 3']
# Create distplot with custom bin_size
fig = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .25, .5])
# Plot!
st.plotly_chart(fig, use_container_width=True)


