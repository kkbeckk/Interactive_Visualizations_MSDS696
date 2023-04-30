# Interactive_Visualizations_MSDS696

The data used was pulled from Kaggle. It's weather data for Australia. Here are the variables in the data:
- Location: Australian City
- MinTemp: Minimum temperature in 24 hour period (°C)
- MaxTemp: Maximum temperature in 24 hour period (°C)
- Rainfall: Precipitation (rainfall) in 24 hour period (mm)
- Evaporation: Evaporation in 24 hour period (mm)
- Sunshine: Sunshine in 24 hour period (hours)
- WindGustDir: Direction of strongest gust in 24 hours
- WindGustSpeed: Speed of strongest gust in 24 hours (kmph)
- WindDir9am: Wind direction averaged over 10 minutes prior to 9 am
- WindDir3pm: Wind direction averaged over 10 minutes prior to 3 pm
- WindSpeed9am: Wind speed averaged over 10 minutes prior to 9 am (kmph)
- WindSpeed3pm: Wind speed averaged over 10 minutes prior to 3 pm (kmph)
- Humidity9am: Relative humidity at 9 am
- Humidity3pm: Relative humidity at 3 pm
- Pressure9am: Atmospheric pressure reduced to mean sea level at 9 am
- Pressure3pm: Atmospheric pressure reduced to mean sea level at 3 pm
- Cloud9am: Fraction of sky obscured by cloud at 9 am
- Cloud3pm:	Fraction of sky obscured by cloud at 3 pm
- Temp9am: Temperature at 9 am
- Temp3pm: Temperature at 3pm
- RainToday: Did it rain today, Yes or No?
- RainTomorrow: Did it rain the next day, Yes or No? 
- Year: Year of observation
- Month: Month of observation

## The 4 python files in this project are:

- MSDS696_BokehTutorial_KelseyBeckwith
This was the tutorial I followed and put together to learn the Bokeh package. This tutorial was completed over weeks 2-3. I learned the different tools that could be created and used within the Bokeh package. Completing this tutorial gave me the base knowledge I needed in order to get started creating my own visuals. 

- DataPreprocessing_EDA_MSDS696_PracticumII
This file was completed during week 4 and part of week 5. Here I am completing the EDA on the data to get a better understanding of it and so I could see what might be interesting to turn into Bokeh visualizations. 

- (FINAL) Temp by City (city selector)
This file is a single bokeh interactive visualization. The reason I have this one standing alone was due to many hours of errors and troubleshooting done with this particualr visual. When combining this visual into my larger worksheet, I was getting data source errors. After spending alont a whole week just on this one visualization, I decided to leave it our of the larger worksheet and to avoid dealing with troubleshooting more errors. 

- (FINAL) Interactive Visualizations
This contains the rest of the final interactive visualizations I created in Bokeh. They are all combine into one workbook, and have thier own named tabs for each. 

## The Bokeh tools used in my visualizaitons and an explaination of what they do:
- Hover: displays informational tooltips
- Crosshair: draws a crosshair annotation over the plot
- Pan: allows the user to pan a Plot by left-dragging a mouse
- Wheel_zoom: zoom the plot in and out, centered on the current mouse location
- Zoom_in: zooms in
- Zoom_out: zooms out
- Box_zoom: zooms in on the selected area
- Undo: undos the last action
- Redo: redos the last action
- Reset: resets the plot to its default 
- Save: allows to save an image reproduction of the plot in PNG format
- Box_select: allows users to make selections on a Plot by showing a rectangular region by dragging the mouse or a finger over the plot area
- Poly_select: allows users to make selections on a Plot by indicating a polygonal region with mouse clicks
- Lasso_select: allows users to make selections on a Plot by indicating a free-drawn “lasso” region by dragging the mouse or a finger over the plot region

## To run the files:
To run either of the (FINAL) Bokeh files, open a terminal and change your directory to your desktop. 
Then run the following:

bokeh serve --show [file name]

After this a window in your browser should appear, showing the visuals. 

## Video Presentation
https://drive.google.com/file/d/1PFN_0hPcfYZmRtGieboPJmW2mVAdhsJU/view?usp=sharing

## References:

Bokeh documentation. Bokeh. (n.d.). Retrieved April 30, 2023, from https://docs.bokeh.org/en/latest/ 

Young, Joe, and Adam Youg. “Rain in Australia.” Kaggle, 2010, https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package. Accessed 10 Feb. 2023. 
<img width="1353" alt="image" src="https://user-images.githubusercontent.com/84113402/235372200-95b284d5-b978-4c75-a2a1-0fa3b0f45096.png">

