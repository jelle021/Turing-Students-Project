
import streamlit as st
import pandas as pd
import plotly_express as px



result = pd.read_csv('result.csv')
timeseries_c = pd.read_csv('timeseries_c.csv')
timeseries_vrate = pd.read_csv('timeseries_vrate.csv')
days_map2 = pd.read_csv('days_map2.csv')



## Data visualization -----------------------------------------------------------------------------------


fig_dailyv = px.line(timeseries_c, x='date', y=["Germany", "France", "Italy", "United Kingdom", "Spain", "Poland", "Romania", "Netherlands" ], 
               labels={
                     "date": "Date(day)",
                     "value": "Cumulative vaccinations",
                     "variable": "Country:"
                 }, title = "Time Series of Cumulative Vaccinations in Europe")

fig_vrate = px.line(timeseries_vrate, x='date', y=["Germany", "France", "Italy", "United Kingdom", "Spain", "Poland", "Romania", "Netherlands" ], 
               labels={
                     "date": "Date(day)",
                     "value": "Vacination rate as % of population",
                     "variable": "Country:"
                 }, title = "Time Series of Vacination Rate in Europe")

## Choropleth
map_series = result.groupby(['country'])['vaccination_rate'].sum()
map_final = map_series.to_frame()
map_final['country'] = map_series.index
map_final.rename(columns = {'vaccination_rate':'Progress'}, inplace = True)
fig_choro = px.choropleth(map_final, locations='country', color='Progress', locationmode='country names',  range_color=[0, 7], title =  'Vaccination Progress World Map')

# Bubble graph with total covid cases - create data frame cases_final line 42

fig_bubble = px.scatter_geo(map_final, locations="country", 
                      #color="Progress",
                     hover_name="country", size="Progress", locationmode='country names', size_max=55, 
                      #range_color=[0, 8], 
                     projection="natural earth")

## prediction on future progress
fig_pred_bubble = px.scatter_geo(days_map2, locations="country", 
                      color="Days Left",
                     hover_name="country", size="Days Since", locationmode='country names', size_max=25, 
                      range_color=[0, 1800], 
                     projection="natural earth")

fig_pred_hist = days_map3['Days Left'].plot(kind='hist', bins=25, title = 'Days Left Worldwide Distribution')


## Streamlit -----------------------------------------------------------------------------------
st.title("Covid-19 Vaccination Progress")
st.text("Hello whatsup guys its working")

## Europe----------------------------------------------------------------------------------------

st.plotly_chart(fig_dailyv)
st.plotly_chart(fig_vrate)
st.plotly_chart(fig_choro)
st.plotly_chart(fig_bubble)
st.plotly_chart(fig_pred_bubble)
## World

