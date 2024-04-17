import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

movies_data = pd.read_csv('https://raw.githubusercontent.com/nv-thang/Data-Visualization-Course/main/movies.csv')

movies_data.info()

movies_data.dropna()

st.title('Interactive Dashboard')
st.header('Interact with this dashboard using the widgets on the sidebar')

st.sidebar.subheader('Select a range on the slider (it represents movie score) to view the total number of movies in a genre that falls within that range')
#st.sidebar.slider('Choose a value',1.00,10.00)
min_value, max_value = 1.00, 10.00
default_values = (min_value, max_value)
selected_values = st.sidebar.slider('Choose a value:', min_value, max_value, default_values, step=0.01)
st.sidebar.subheader('Select your preferred genre(s) and year to view the movies released that year and on that genre')
st.sidebar.multiselect('Choose Genre',['Drama','Adventure','Action','Horror','Biography','Crime','Fantasy','Animation','Romance','Music','Western','Thriller','History','Mystery','Sport','Musical'])
st.sidebar.selectbox('Choose a year',[1980,1981,1982,1983,1984,1985,1986,1987,1989,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020])

selected_genre = st.sidebar.multiselect('Choose Genre', movies_data['genre'].unique())
selected_year = st.sidebar.selectbox('Choose a year', movies_data['year'].unique())


avg_budget = movies_data.groupby('genre')['budget'].mean().round()
avg_budget = avg_budget.reset_index()
genre = avg_budget['genre']
avg_bud = avg_budget['budget']

st.write("""User score of movies and their genre""")

line = plt.figure(figsize=(19,10))
plt.plot(genre,avg_bud,linestyle='-')
plt.grid(c='white')
plt.gca().set_facecolor('black')
plt.xticks(genre, rotation=45)
plt.xlabel('genre')
plt.ylabel('score')

st.pyplot(line)

st.write("""Average Movie Budget, Grouped by Genre""")


fig = plt.figure(figsize=(19,10))

plt.bar(genre, avg_bud, color = 'maroon')
plt.xlabel('genre')
plt.ylabel('budget')
plt.title('Matplotlib Bar Chart Showing the Average \ Budget of Movies in Each Genre')

st.pyplot(fig)

