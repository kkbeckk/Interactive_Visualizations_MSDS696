#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import bokeh.sampledata
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta, date
import datetime

from bokeh.plotting import figure, show, output_file, save, output_notebook
from bokeh.models import Div, RangeSlider, Spinner, BoxAnnotation, NumeralTickFormatter, DatetimeTickFormatter
from bokeh.layouts import layout, row, gridplot, column
from bokeh.io import curdoc
from bokeh.models.tools import BoxZoomTool, ResetTool, PanTool
from bokeh.palettes import Turbo256, Blues4
from bokeh.transform import linear_cmap
from bokeh.models import ColumnDataSource, CDSView, IndexFilter, GroupFilter, HoverTool, DataRange1d, Select
from os.path import dirname, join
from scipy.signal import savgol_filter
import os
from bokeh.models.widgets import DateSlider, Slider, RangeSlider
from bokeh.models import CustomJS


# # Temp by City (City Dropdown)

# In[2]:


city = 'Albury'

cities = {'Albury': {'Location': 'Albury','title': 'Albury, AUS'},
    'Uluru': {'Location': 'Uluru','title': 'Uluru, AUS'},
    'Darwin': {'Location': 'Darwin','title': 'Darwin, AUS'},
    'Perth': {'Location': 'Perth','title': 'Perth, AUS'},
    'SalmonGums': {'Location': 'SalmonGums','title': 'SalmonGums, AUS'},
    'MountGinini': {'Location': 'MountGinini','title': 'MountGinini, AUS'},
    'Albany': {'Location': 'Albany','title': 'Albany, AUS'},
    'Wollongong': {'Location': 'Wollongong','title': 'Wollongong, AUS'},
    'WaggaWagga': {'Location': 'WaggaWagga','title': 'WaggaWagga, AUS'},
    'AliceSprings': {'Location': 'AliceSprings','title': 'AliceSprings, AUS'},
    'Townsville': {'Location': 'Townsville','title': 'Townsville, AUS'},
    'Cairns': {'Location': 'Cairns','title': 'Cairns, AUS'},
    'Mildura': {'Location': 'Mildura','title': 'Mildura, AUS'},
    'Sydney': {'Location': 'Sydney','title': 'Sydney, AUS'}}       
        


# In[3]:


df = pd.read_csv('/Users/kelsey/Desktop/mastersDataSci/Data Science Practicum II - MSDS696/data/raindata.csv')


# In[4]:


Statistics = ['MaxTemp', 'MinTemp', 'Temp3pm', 'Temp9am', 'Humidity3pm', 'Humidity9am']


# In[5]:


def get_dataset(src, name):
    df = src[src.Location == name].copy()
    df['Date'] = pd.to_datetime(df[['Year', 'Month']].assign(DAY=1))
    df['Date'] = df['Date'].astype(object)
    df['Date'] = pd.to_datetime(df['Date'])
    df['left'] = df['Date'] - datetime.timedelta(days=30)
    df['right'] = df['Date'] + datetime.timedelta(days=30)
    df = df.set_index(['Date'])
    df.sort_index(inplace=True)
   
    return ColumnDataSource(data = df)


# In[6]:


source = get_dataset(df, cities[city]['Location'])

plot = figure(x_axis_type = "datetime", width = 800, toolbar_location = "below", 
              x_range = (2008,2018), y_range = (0, 55), sizing_mode="stretch_width")

plot.quad(top = 'MaxTemp', bottom = 'MinTemp', left = 'left', right = 'right', alpha = 0.5, 
          source = source, legend_label = "Max and Min Temp", color =  "maroon")

plot.quad(top = 'Temp3pm', bottom = 'Temp9am', left = 'left', right = 'right', alpha = 0.5, 
          source = source, legend_label = "Morning and Afternoon Temp", color = "mediumpurple")

plot.xaxis.axis_label = None
plot.yaxis.axis_label = "Tempurature (°C)"
plot.axis.axis_label_text_font_style = "bold"
plot.x_range = DataRange1d(range_padding=0.0)
plot.grid.grid_line_alpha = 0.3

low_box = BoxAnnotation(top=20, fill_alpha=0.2, fill_color="dimgray")
mid_box = BoxAnnotation(bottom=20, top=40, fill_alpha=0.2, fill_color="silver")
high_box = BoxAnnotation(bottom=40, fill_alpha=0.2, fill_color="dimgray")

plot.add_layout(low_box)
plot.add_layout(mid_box)
plot.add_layout(high_box)

city_select = Select(value=city, title='City', options=sorted(cities.keys()))


# In[7]:


def update_plot(attrname, old, new):
    city = city_select.value
    src = get_dataset(df, cities[city]['Location'])
    source.data.update(src.data)

date_slider = DateSlider(title="Date", value=date(2014, 1, 1), start=date(2008, 1, 1), 
                         end=date(2018, 1, 1), step=365)
rel_date = date_slider.value
date_slider.on_change('value', update_plot)

city_select.on_change('value', update_plot)

layout = column(plot, city_select, date_slider)

sizing_mode = "strech_width"
curdoc().add_root(layout, sizing_mode)


# In[ ]:




