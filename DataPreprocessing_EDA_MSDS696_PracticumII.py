#!/usr/bin/env python
# coding: utf-8

# # Interactive Visualizations with Bokeh
# 
# ## Importing needed Libraries

# In[1]:


import pandas as pd
import numpy as np
import bokeh.sampledata
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import datetime


# ## Import the Data

# In[2]:


df = pd.read_csv('raindata.csv')


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


print(df.shape)


# In[6]:


df.describe().T


# In[7]:


df.describe(include=[object]).T


# ## EDA

# In[8]:


df['RainTomorrow'].value_counts().plot(kind='bar')


# In[9]:


df.RainTomorrow = df.RainTomorrow.map({'No':0, 'Yes':1}).astype('float64')


# In[10]:


corr = df.corr()
corr.style.background_gradient()

plt.figure(figsize=(50,20))
sns.heatmap(corr,annot=True,cmap='Greens')


# In[11]:


fig, ax = plt.subplots(4, 2, figsize = (10, 20))
sns.kdeplot(x = df.WindSpeed9am, ax = ax [0, 0], shade = True)
sns.kdeplot(x = df.WindSpeed3pm, ax = ax[0, 1], shade = True)
sns.kdeplot(x = df.Humidity9am, ax = ax[1, 0], shade = True)
sns.kdeplot(x = df.Humidity3pm, ax = ax[1, 1], shade = True)
sns.kdeplot(x = df.Pressure9am, ax = ax[2, 0], shade=True)
sns.kdeplot(x = df.Pressure3pm, ax = ax[2, 1], shade=True)
sns.kdeplot(x = df.Cloud9am, ax = ax[3, 0], shade=True)
sns.kdeplot(x = df.Cloud3pm, ax = ax[3, 1], shade=True);


# In[12]:


fig, ax = plt.subplots(2, 2, figsize = (10, 10))
sns.lineplot(data = df, x = 'Sunshine', y = 'Rainfall', ax = ax [0, 0])
sns.lineplot(data = df, x = 'Evaporation', y = 'Rainfall', ax = ax [0, 1])
sns.lineplot(data = df, x = 'Humidity3pm', y = 'Rainfall', ax = ax [1, 0])
sns.lineplot(data = df, x = 'Cloud3pm', y = 'Rainfall', ax = ax [1, 1]);


# In[13]:


loc_temp = df.groupby(['Location'])['MaxTemp'].median().reset_index()
plt.figure(figsize = (12, 5))
loc = sns.barplot(data = loc_temp, y = 'MaxTemp', x = 'Location', order = loc_temp.sort_values('MaxTemp').Location)
loc.set_xticklabels(loc.get_xticklabels(), rotation = 65, horizontalalignment = 'right');


# In[14]:


fig, (plot1) = plt.subplots(1, figsize = (12, 5))
monthly = df.groupby(['Month'])['Rainfall'].sum().reset_index()
plot1.plot(monthly.Month, monthly.Rainfall)
plot1.set_xlabel('Month')
plot1.set_ylabel('Rain (mm)');


# In[15]:


fig, (plot2) = plt.subplots(1, figsize = (12, 5))
yearly = df.groupby(['Year'])['Rainfall'].sum().reset_index()
plot2.plot(yearly.Year, yearly.Rainfall)
plot2.set_xlabel('Year')
plot2.set_ylabel('Rain (mm)');


# In[16]:


sns.set(rc = {'figure.figsize':(12,12)})
pop = sns.scatterplot(data = df,x = 'Humidity3pm', y = 'Temp3pm', hue = 'Rainfall', palette = 'Set2')
pop.legend(loc = 'center left', bbox_to_anchor = (1.25, 0.5), ncol = 1)


# # Interactive Visualizations with Bokeh

# from bokeh.plotting import figure, show, output_file, save, output_notebook
# from bokeh.models import Div, RangeSlider, Spinner, BoxAnnotation, NumeralTickFormatter, DatetimeTickFormatter
# from bokeh.layouts import layout, row, gridplot, column
# from bokeh.io import curdoc
# from bokeh.models.tools import BoxZoomTool, ResetTool, PanTool
# from bokeh.palettes import Turbo256, Blues4
# from bokeh.transform import linear_cmap
# from bokeh.models import ColumnDataSource, CDSView, IndexFilter, GroupFilter, HoverTool, DataRange1d, Select
# from os.path import dirname, join
# from scipy.signal import savgol_filter
# 
# from bokeh.models.widgets import CheckboxGroup

# ## Yearly Rainfall

# curdoc().theme = "contrast"

# yearly = df.groupby(['Year'])['Rainfall'].sum().reset_index()

# evapo = df.groupby(['Year'])['Evaporation'].sum().reset_index()

# x = yearly.Year
# y = yearly.Rainfall
# 
# x1 = evapo.Year
# y1 = evapo.Evaporation
# 
# Yearly_Rain = figure(x_range = (2006,2018), width = 900, height = 500, 
#                       title = "Total Yearly Rainfall & Evaporation in Australia", 
#                       x_axis_label='Year', y_axis_label='Rainfall (mm)', tooltips = "measured in (mm)",
#                      background_fill_color = "#3b527a")
# 
# points = Yearly_Rain.circle(x = x1, y = y1, size = 20, fill_color = "#21a7df", legend_label = "Evaporation",
#                              fill_alpha=0.5)
# line = Yearly_Rain.line(x = x, y = y, color = "#040252", line_width = 3, legend_label = "Rainfall")
# 
# div = Div(text = """<p>Select the circle's size using this control element:</p>""", width = 200, height = 30)
# 
# spinner = Spinner(title = "Circle Size", low = 15, high = 45, step = 5, value = points.glyph.size, width = 200)
# spinner.js_link("value", points.glyph, "size")
# 
# 
# range_slider = RangeSlider(title = "Adjust x-axis range", start = 0, end = 13, step = 1, 
#                            value=(Yearly_Rain.x_range.start, Yearly_Rain.x_range.end))
# 
# range_slider.js_link("value", Yearly_Rain.x_range, "start", attr_selector = 0)
# range_slider.js_link("value", Yearly_Rain.x_range, "end", attr_selector = 1)
# 

# Yearlayout = layout([[div, spinner], [range_slider], [Yearly_Rain]])
# 
# show(Yearlayout)

# # Weather Distribution by Location

# df['Date'] = pd.to_datetime(df[['Year', 'Month']].assign(DAY=1))
# df = df['Date'].astype({'Date':'str'})

# 
# 
# def make_plot(source, title):
#     plot = figure(x_axis_type = 'datetime', width = 800, tools = '', toolbar_location = None)
#     plot.title.text = title
# 
#     plot.quad(top = 'MaxTemp', bottom = 'MinTemp', left = 'left', right = 'right',
#               color = Blues4[2], source = source, legend_label = 'Max and Min')
#     plot.quad(top = 'Temp3pm', bottom = 'Temp9am', left = 'left', right = 'Morning and Afternoon',
#               color = Blues4[1], source = source, legend_label = 'Average')
#     plot.quad(top = 'Humidity3pm', bottom = 'Humidity9am', left = 'left', right = 'right',
#               color = Blues4[0], alpha = 0.5, line_color = 'black', source = source, legend_label = 'Humidity')
# 
#     # fixed attributes
#     plot.xaxis.axis_label = None
#     plot.yaxis.axis_label = 'Temperature (F)'
#     plot.axis.axis_label_text_font_style = 'bold'
#     plot.x_range = DataRange1d(range_padding = 0.0)
#     plot.grid.grid_line_alpha = 0.3
# 
#     return plot
# 
# 
# def update_plot(attrname, old, new):
#     city = city_select.value
#     plot.title.text = "Weather data for " + df.Location
# 
#     src = get_dataset(df, df['Location'], distribution_select.value)
#     source.data.update(src.data)
# 
# distribution = 'Discrete'
# 
# city_select = Select(value=df['Location'], title='Location')
# distribution_select = Select(value=distribution, title='Distribution', options=['Discrete', 'Smoothed'])
# 
# source = get_dataset(df, df['Location'], distribution)
# plot = make_plot(source, "Weather data for " + df.Location)
# 
# city_select.on_change('value', update_plot)
# distribution_select.on_change('value', update_plot)
# 
# controls = column(city_select, distribution_select)
# 
# curdoc().add_root(row(plot, controls))
# curdoc().title = "Weather"
# 

# Statistics = ['MaxTemp', 'MinTemp', 'Temp3pm', 'Temp9am', 'Humidity3pm', 'Humidity9am']
# 
# def get_dataset(src, name, distribution):
#     df = src[src.Location == name].copy()
#     del df['Location']
#     df['Date'] = pd.to_datetime(df.Date)
#     df['left'] = df.Date - datetime.timedelta(days=0.5)
#     df['right'] = df.Date + datetime.timedelta(days=0.5)
#     df = df.set_index(['Date'])
#     df.sort_index(inplace=True)
#     if distribution == 'Smoothed':
#         window, order = 51, 3
#         for key in STATISTICS:
#             df[key] = savgol_filter(df[key], window, order)
# 
#     return ColumnDataSource(data=df)
# 
# def make_plot(source, title):
#     plot = figure(x_axis_type = 'datetime', width = 800, tools = "", toolbar_location = None)
#     plot.title.text = title
#     
#     plot.quad(top = 'MaxTemp', bottom = 'MinTemp', left = 'left', right = 'right',
#               color = Blues4[2], source = source, legend_label = 'Max and Min')
#     plot.quad(top = 'Temp3pm', bottom = 'Temp9am', left = 'left', right = 'Morning and Afternoon',
#               color = Blues4[1], source = source, legend_label = 'Average')
#     plot.quad(top = 'Humidity3pm', bottom = 'Humidity9am', left = 'left', right = 'right',
#               color = Blues4[0], alpha = 0.5, line_color = 'black', source = source, legend_label = 'Humidity')
# 
#     # fixed attributes
#     plot.xaxis.axis_label = None
#     plot.yaxis.axis_label = 'Temperature (F)'
#     plot.axis.axis_label_text_font_style = 'bold'
#     plot.x_range = DataRange1d(range_padding=0.0)
#     plot.grid.grid_line_alpha = 0.3
# 
#     return plot
# 
# def update_plot(attrname, old, new):
#     city = city_select.value
#     plot.title.text = "Weather data for " + df.Location
# 
#     src = get_dataset(df, df['Location'], distribution_select.value)
#     source.data.update(src.data)
# 
# city = 'Albury'
# distribution = 'Discrete'
# 
# cities = {
#     'Albury': {
#         'Location': 'ABX',
#         'title': 'Albury, AUS',
#     },
#     'BadgerysCreek': {
#         'Location': 'WSI',
#         'title': 'BadgerysCreek, AUS',
#     },
#     'Cobar': {
#         'Location': 'CAZ',
#         'title': 'Cobar, AUS',
#     },
#     'CoffsHarbour': {
#         'Location': 'CFS',
#         'title': 'CoffsHarbour, AUS',
#     },
#     'Moree': {
#         'Location': 'MRZ',
#         'title': 'Moree, AUS',
#     },
#     'Newcastle': {
#         'Location': 'NTL',
#         'title': 'Newcastle, AUS',
#     },
#     'NorfolkIsland': {
#         'Location': 'NF',
#         'title': 'NorfolkIsland, AUS',
#     },
#     'Richmond': {
#         'Location': 'RIC',
#         'title': 'Richmond, AUS',
#     },
#     'Sydney': {
#         'Location': 'SYD',
#         'title': 'Sydney, AUS'}
# }
# 
# 
#     
# city_select = Select(value = city, title = 'City', options = sorted(cities.keys()))
# distribution_select = Select(value = distribution, title = 'Distribution', options = ['Discrete', 'Smoothed'])
# 
# df = pd.read_csv(join(dirname(__file__), 'data/2015_weather.csv'))
# source = get_dataset(df, cities[city]['Location'], distribution)
# plot = make_plot(source, "Weather data for " + cities[city]['title'])
# 
# city_select.on_change('value', update_plot)
# distribution_select.on_change('value', update_plot)
# 
# controls = column(city_select, distribution_select)
# 
# curdoc().add_root(row(plot, controls))
# curdoc().title = "Weather"

# NorahHead
# Penrith
# 
# 
# 
# 
# WaggaWagga
# Williamtown
# Wollongong
# Canberra
# Tuggeranong
# MountGinini
# Ballarat
# Bendigo
# Sale
# MelbourneAirport
# Melbourne
# Mildura
# Nhil
# Portland
# Watsonia
# Dartmoor
# Brisbane
# Cairns
# GoldCoast
# Townsville
# Adelaide
# MountGambier
# Nuriootpa
# Woomera
# Albany
# Witchcliffe
# PearceRAAF
# PerthAirport
# Perth
# SalmonGums
# Walpole
# Hobart
# Launceston
# AliceSprings
# Darwin
# Katherine
# Uluru

# In[ ]:




