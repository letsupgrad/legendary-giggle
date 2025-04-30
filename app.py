import streamlit as st
from bokeh.plotting import figure
from bokeh.palettes import Category10
from bokeh.transform import cumsum
from bokeh.layouts import column
import pandas as pd
import numpy as np
from math import pi

st.set_page_config(page_title="Bokeh Chart Gallery", layout="wide")
st.title("📊 Bokeh Chart Gallery in Streamlit")

# Sample Data
x = list(range(10))
y = [np.random.randint(1, 10) for _ in x]
categories = ['A', 'B', 'C', 'D']
values = np.random.randint(10, 100, size=4)

# Line Chart
def line_chart():
    p = figure(title="Line Chart", width=500, height=350)
    p.line(x, y, line_width=2, color="green", legend_label="Line")
    return p

# Bar Chart
def bar_chart():
    p = figure(x_range=categories, title="Bar Chart", width=500, height=350)
    p.vbar(x=categories, top=values, width=0.6, color=Category10[4])
    return p

# Scatter Plot
def scatter_chart():
    p = figure(title="Scatter Plot", width=500, height=350)
    p.circle(x, y, size=10, color="red", alpha=0.6)
    return p

# Pie Chart
def pie_chart():
    data = pd.Series(values, index=categories)
    data = data / data.sum() * 2 * pi
    df = pd.DataFrame({'angle': data, 'color': Category10[4], 'category': categories})
    p = figure(title="Pie Chart", width=500, height=350, toolbar_location=None, tools="hover", tooltips="@category", x_range=(-0.5, 1.0))
    p.wedge(x=0, y=1, radius=0.4, start_angle=cumsum('angle', include_zero=True),
            end_angle=cumsum('angle'), line_color="white", fill_color='color', legend_field='category', source=df)
    p.axis.visible = False
    return p

# Area Chart
def area_chart():
    p = figure(title="Area Chart", width=500, height=350)
    p.varea(x=x, y1=[0]*len(x), y2=y, fill_color="skyblue", alpha=0.5)
    return p

# Histogram
def histogram_chart():
    hist_data = np.random.normal(0, 1, 1000)
    hist, edges = np.histogram(hist_data, bins=20)
    p = figure(title="Histogram", width=500, height=350)
    p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], fill_color="purple", alpha=0.7)
    return p

# Display all charts
st.bokeh_chart(column(
    line_chart(),
    bar_chart(),
    scatter_chart(),
    pie_chart(),
    area_chart(),
    histogram_chart()
))
