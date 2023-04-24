#!/usr/bin/env python
# coding: utf-8

# # Measurements for Weather in Australia

# In[1]:


from bokeh.plotting import figure, show, output_file, save, output_notebook
from bokeh.models import Div, RangeSlider, Spinner, BoxAnnotation, NumeralTickFormatter, DatetimeTickFormatter
from bokeh.layouts import layout, row, gridplot, column
from bokeh.io import curdoc
from bokeh.models.tools import BoxZoomTool, ResetTool, PanTool
from bokeh.palettes import Turbo256, Blues4, Cividis
from bokeh.transform import linear_cmap
from bokeh.models import ColumnDataSource, CDSView, IndexFilter, GroupFilter, HoverTool, DataRange1d, Select
import pandas as pd
from bokeh.models import Panel, Tabs, CustomJS, Dropdown

from datetime import datetime, timedelta, date
import datetime
from os.path import dirname, join
import os
from bokeh.models.widgets import DateSlider, Slider, RangeSlider


# In[2]:


df = pd.read_csv('/Users/kelsey/Desktop/raindata2.csv')


# In[3]:


monthly = df.groupby(['Month'])['Rainfall'].sum().reset_index()
evapor = df.groupby(['Month'])['Evaporation'].sum().reset_index()


# # Monthly Rain & Evaporation

# In[4]:


month = monthly.Month
rain = monthly.Rainfall
evapo = evapor.Evaporation

source = ColumnDataSource(data= {'x' : month, 'y' : rain})

def update_plot(attr, old, new):
    if new == 'Rainfall':
        source.data['y'] = rain
        p.yaxis.axis_label = 'Rainfall'
    else:
        source.data['y'] = evapo
        p.yaxis.axis_label = 'Evaporation'

menu = Select(options=[('Rainfall','Rainfall'), ('Evaporation','Evaporation')],
              value='Rainfall',
              title = 'Weather Elements')

menu.on_change('value', update_plot)

p = figure(x_axis_type='auto', title = 'Total Yearly Rainfall & Evaporation in Australia', x_axis_label='Month',
          y_axis_label='(mm)')
p.line('x',
       'y',
       source=source,
       color='green',
       width=3)

layout1 = column(p, menu)


tab1 = Panel(child = layout1, title = "Monthly")


# In[ ]:





# month = monthly.Month
# rain = monthly.Rainfall
# evapo = evapor.Evaporation
# 
# source = ColumnDataSource(data= {'x' : month, 'y' : rain})
# 
# # called when the Select item changes in value
# def update_plot(event):
#     if event.item == 'Rainfall':
#         source.data['y'] = rain
#         p.yaxis.axis_label = 'Rainfall'
#     else:
#         source.data['y'] = evapo
#         p.yaxis.axis_label = 'Evaporation'
# 
# # update the date source
# source.data = df
# 
# # display a Dropdown menu
# menu = Dropdown(label="Select Measurement",
#                 menu=[
#                     ('Rainfall','Rainfall'),
#                     ('Evaporation','Evaporation'),
#                     ])
# 
# # callback when the Dropdown menu is selected
# menu.on_click(update_plot)
# 
# p = figure(x_axis_type='auto', title = 'Total Yearly Rainfall & Evaporation in Australia', x_axis_label='Month',
#           y_axis_label='(mm)')
# p.line('x',
#        'y',
#        source=source,
#        color='green',
#        width=3)
# 
# monthly = column(p, menu)
# 
# 
# tab1 = Panel(child = monthly, title = "Monthly")

# # Annual Rain & Evaporation

# In[5]:


yearly = df.groupby(['Year'])['Rainfall'].sum().reset_index()
evapo = df.groupby(['Year'])['Evaporation'].sum().reset_index()


# In[6]:


year = yearly.Year
yrain = yearly.Rainfall
yevapo = evapo.Evaporation

source = ColumnDataSource(data= {'x' : year, 'y' : yrain})

Yearly_Rain = figure(x_range = (2006,2018), width = 900, height = 500, 
                      title = "Total Yearly Rainfall & Evaporation in Australia", 
                      x_axis_label='Year', y_axis_label='Rainfall (mm)', tooltips = "measured in (mm)",
                     background_fill_color = "#3b527a")

points = Yearly_Rain.circle(x = year, y = yevapo, size = 20, fill_color = "#21a7df", legend_label = "Evaporation",
                             fill_alpha=0.5)
line = Yearly_Rain.line(x = year, y = yrain, color = "#040252", line_width = 3, legend_label = "Rainfall")

div = Div(text = """<p>Select the circle's size using this control element:</p>""", width = 200, height = 30)

spinner = Spinner(title = "Circle Size", low = 15, high = 45, step = 5, value = points.glyph.size, width = 200)
spinner.js_link("value", points.glyph, "size")


range_slider = RangeSlider(title = "Adjust x-axis range", start = 0, end = 13, step = 1, 
                           value=(Yearly_Rain.x_range.start, Yearly_Rain.x_range.end))

range_slider.js_link("value", Yearly_Rain.x_range, "start", attr_selector = 0)
range_slider.js_link("value", Yearly_Rain.x_range, "end", attr_selector = 1)

layout2 = layout([[div, spinner], [range_slider], [Yearly_Rain]])

tab2 = Panel(child = layout2, title = "Yearly")


# # Temp by City (City Dropdown)
# 
# Currently this is not returning the correct data in the tabs. Works on it's own

# In[7]:


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


# In[8]:


df3 = pd.read_csv('/Users/kelsey/Desktop/mastersDataSci/Data Science Practicum II - MSDS696/data/raindata.csv')
Statistics = ['MaxTemp', 'MinTemp', 'Temp3pm', 'Temp9am', 'Humidity3pm', 'Humidity9am']


# In[9]:


def get_dataset(src, name): #, distribution):
    df3 = src[src.Location == name].copy()
    df3['Date'] = pd.to_datetime(df3[['Year', 'Month']].assign(DAY=1))
    df3['Date'] = df3['Date'].astype(object)
    df3['Date'] = pd.to_datetime(df3['Date'])
    df3['left'] = df3['Date'] - datetime.timedelta(days=30)
    df3['right'] = df3['Date'] + datetime.timedelta(days=30)
    df3 = df3.set_index(['Date'])
    df3.sort_index(inplace=True)

    return ColumnDataSource(data = df3)


# In[10]:


source = get_dataset(df3, cities[city]['Location'])
plot = figure(x_axis_type = "datetime", width = 800, toolbar_location = "below", x_range = (2008,2018),
             background_fill_color = "#3b527a", y_range = (0, 60))    

plot.quad(top = 'MaxTemp', bottom = 'MinTemp', left = 'left', right = 'right', alpha = 0.5, 
          source = source, legend_label = "Max and Min Temp", color =  "maroon")

plot.quad(top = 'Temp3pm', bottom = 'Temp9am', left = 'left', right = 'right', alpha = 0.5, 
          source = source, legend_label = "Morning and Afternoon Temp", color = "mediumpurple")

plot.xaxis.axis_label = None
plot.yaxis.axis_label = None
plot.axis.axis_label_text_font_style = "bold"
plot.x_range = DataRange1d(range_padding=0.0)
plot.grid.grid_line_alpha = 0.3
#plot.legend.location = "top_l"

city_select = Select(value=city, title='City', options=sorted(cities.keys()))


# In[11]:


def update_plot(attrname, old, new):
    city = city_select.value
    src = get_dataset(df3, cities[city]['Location'])
    source.data.update(src.data)

date_slider = DateSlider(title="Date", value=date(2014, 1, 1), start=date(2008, 1, 1), 
                         end=date(2018, 1, 1), step=365)
rel_date = date_slider.value
date_slider.on_change('value', update_plot)

city_select.on_change('value', update_plot)

layout3 = column(plot, city_select, date_slider)


#curdoc().add_root(layout)


# In[12]:


tab3 = Panel(child = layout3, title = "City's Temps")


# # Total Yearly Rain (Stacked)

# In[13]:


df4 = pd.read_csv('/Users/kelsey/Desktop/rain_by_year(2).csv')


# In[14]:


total_year = figure(x_range=(2013,2017), y_range=(0, 1000))
total_year.grid.minor_grid_line_color = '#eeeeee'

names = ['Albany', 'Albury', 'AliceSprings', 'Cairns', 'Darwin']
total_year.varea_stack(stackers=names, x='Unnamed: 0', color=Cividis[5], legend_label=names, source=df4)

total_year.legend.orientation = "horizontal"
total_year.legend.background_fill_color = "#fafafa"


# In[15]:


tab4 = Panel(child = total_year, title = "Yearly Rain (stacked)")


# In[16]:


tabs = Tabs(tabs=[tab1,tab2, tab3, tab4])

curdoc().theme = 'night_sky'
curdoc().add_root(column(tabs))
curdoc().title = "Australia Weather"


# In[ ]:




