#!/usr/bin/env python
# coding: utf-8

# # Measurements for Weather in Australia

# In[1]:


from bokeh.plotting import figure, show, output_file, save, output_notebook
from bokeh.models import Div, RangeSlider, Spinner, BoxAnnotation, NumeralTickFormatter, DatetimeTickFormatter
from bokeh.layouts import layout, row, gridplot, column
from bokeh.io import curdoc
from bokeh.models.tools import BoxZoomTool, ResetTool, PanTool
from bokeh.palettes import Turbo256, Blues4, Cividis, Blues3
from bokeh.transform import linear_cmap, factor_cmap
from bokeh.models import ColumnDataSource, CDSView, IndexFilter, GroupFilter, HoverTool, DataRange1d, Select
import pandas as pd
from bokeh.models import Panel, Tabs, CustomJS, Dropdown

from datetime import datetime, timedelta, date
import datetime
from os.path import dirname, join
import os
from bokeh.models.widgets import DateSlider, Slider, RangeSlider
import numpy as np


# In[2]:


df = pd.read_csv('/Users/kelsey/Desktop/raindata2.csv')


# In[3]:


monthly = df.groupby(['Month'])['Rainfall'].sum().reset_index()
evapor = df.groupby(['Month'])['Evaporation'].sum().reset_index()


# In[4]:


TOOLS = "hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,save,box_select,poly_select,lasso_select"


# # Monthly Rain & Evaporation

# In[5]:


month = monthly.Month
rain = monthly.Rainfall
evapo = evapor.Evaporation

source = ColumnDataSource(data= {'x' : month, 'y' : rain})

p = figure(x_axis_type='auto', title = 'Total Monthly Rainfall in Australia', x_axis_label='Month',
           y_axis_label='(mm)', sizing_mode="stretch_width",
           tooltips="The @x month of the year had a total rainfall of @y mm", tools = TOOLS)
p.line('x',
       'y',
       source=source,
       color='green',
       width=3)

source2 = ColumnDataSource(data={'x' : month, 'y' : evapo})
p2= figure(x_axis_type='auto', title = 'Total Monthly Evaporation in Australia', x_axis_label='Month', 
           y_axis_label='(mm)', sizing_mode="stretch_width", tools=[HoverTool()], 
           tooltips="The @x month of the year had a total evaporation of @y mm")
p2.line('x',
       'y',
       source=source2,
       color='green',
       width=3)

layout1 = row(children=[p, p2], sizing_mode="scale_width")


tab1 = Panel(child = layout1, title = "Monthly")


# # Annual Rain & Evaporation

# In[6]:


yearly = df.groupby(['Year'])['Rainfall'].sum().reset_index()
evapo = df.groupby(['Year'])['Evaporation'].sum().reset_index()


# In[7]:


year = yearly.Year
yrain = yearly.Rainfall
yevapo = evapo.Evaporation

source = ColumnDataSource(data= {'x' : year, 'y' : yrain})

Yearly_Rain = figure(x_range = (2006,2018), width = 900, height = 500, 
                     title = "Total Yearly Rainfall & Evaporation in Australia", sizing_mode="stretch_width",
                     x_axis_label='Year', y_axis_label='Rainfall (mm)',
                     tooltips="Measured in millimeters", tools = TOOLS)

points = Yearly_Rain.circle(x = year, y = yevapo, size = 20, fill_color = "#21a7df", legend_label = "Evaporation",
                             fill_alpha=0.5)
line = Yearly_Rain.line(x = year, y = yrain, color = "#040252", line_width = 3, legend_label = "Rainfall")

div = Div(text = """<p>Select the circle's size using this control element:</p>""", width = 200, height = 30)

spinner = Spinner(title = "Circle Size", low = 15, high = 45, step = 5, value = points.glyph.size, width = 200)
spinner.js_link("value", points.glyph, "size")


#range_slider = RangeSlider(title = "Adjust x-axis range", start = 0, end = 13, step = 1, 
#                           value=(Yearly_Rain.x_range.start, Yearly_Rain.x_range.end))

#range_slider.js_link("value", Yearly_Rain.x_range, "start", attr_selector = 0)
#range_slider.js_link("value", Yearly_Rain.x_range, "end", attr_selector = 1)

layout2 = layout([[div, spinner], [Yearly_Rain]], sizing_mode='stretch_width')

tab2 = Panel(child = layout2, title = "Yearly")


# # Total Yearly Rain (Stacked)

# In[8]:


df4 = pd.read_csv('/Users/kelsey/Desktop/rain_by_year(2).csv')


# In[9]:


total_year = figure(x_range=(2013, 2017), y_range=(0, 2000), sizing_mode="stretch_width", tools= TOOLS)

names = ['Albany', 'AliceSprings', 'Cairns', 'Darwin', 'Melbourne', 'Mildura', 'MountGinini', 
         'NorfolkIsland','Perth', 'Sydney']
total_year.varea_stack(stackers=names, x='Unnamed: 0', color=Cividis[10], legend_label=names, source=df4)

total_year.yaxis.axis_label = "Total Rainfall (mm)"
total_year.legend.orientation = "horizontal"
total_year.legend.background_fill_color = "#fafafa"


# In[10]:


tab3 = Panel(child = total_year, title = "Yearly Rain (stacked)")


# # Yearly Rainfall

# In[11]:


totalRain = pd.read_csv('/Users/kelsey/Desktop/raindata.csv')


# In[12]:


total_rain_year = df.groupby(['Year'])['Rainfall'].sum().reset_index()

x = totalRain.Year.unique()
y = total_rain_year


# In[13]:


source = ColumnDataSource(total_rain_year)

p = figure(plot_width=400, plot_height=400, sizing_mode="stretch_width", 
           tooltips="In the year @x Australia had a total of @y mm in rain", tools = TOOLS)

p.vbar(x = 'Year', top = 'Rainfall', source = source, width = .4, bottom = 0, color = 'cadetblue')
p.y_range.start = 0
p.yaxis.axis_label = "Rainfall (mm)"
p.yaxis[0].formatter = NumeralTickFormatter(format="0000")

tab4 = Panel(child = p, title = "Australia's Yearly Rainfall")


# # Pressure vs Temp

# In[14]:


df5 = pd.read_csv('/Users/kelsey/Desktop/raindata.csv')


# In[15]:


x= df5['Temp9am']
y= df5['Pressure9am']


# In[16]:


press = figure(plot_width=500,plot_height=800,tools=TOOLS, sizing_mode='stretch_width')
press.title.text= 'Temperature and Air Pressure'
press.title.text_color= 'Gray'
press.title.text_font= 'arial'
press.title.text_font_style= 'bold'
press.xaxis.minor_tick_line_color= None
press.yaxis.minor_tick_line_color= None
press.xaxis.axis_label='Temperature (°C)'
press.yaxis.axis_label='Pressure (hPa)' 

press.circle(df5['Temp9am'],df5['Pressure9am'],size=0.7, color = 'cadetblue')


# In[17]:


tab5 = Panel(child = press, title = 'Pressure V. Temp')


# In[ ]:





# In[18]:


tabs = Tabs(tabs=[tab1, tab2, tab3, tab4, tab5], sizing_mode='stretch_width')

curdoc().theme = 'light_minimal'
curdoc().add_root(column(tabs))
curdoc().title = "Australia Weather"


# In[ ]:





# In[ ]:




