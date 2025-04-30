import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
import plotly.express as px
from bokeh.plotting import figure
from bokeh.transform import cumsum
from bokeh.palettes import Category10
from math import pi
from bokeh.models import ColumnDataSource

# Load sample data
iris = load_iris(as_frame=True)
df = iris.frame

st.set_page_config(page_title="📊 Dashboard with Bokeh & Plotly", layout="wide")
st.title("📈 Dashboard: All Chart Types (Bokeh + Plotly)")

st.sidebar.title("Chart Options")
chart_type = st.sidebar.selectbox("Select chart type", [
    "Plotly Line Chart", "Plotly Bar Chart", "Plotly Scatter Plot", "Plotly Box Plot", "Plotly Pie Chart",
    "Bokeh Line Chart", "Bokeh Area Chart", "Bokeh Pie Chart", "Bokeh Histogram"
])

# =========================
# PLOTLY CHARTS
# =========================
if chart_type == "Plotly Line Chart":
    fig = px.line(df, x="sepal length (cm)", y="sepal width (cm)", color=iris.target_names[df.target[0]])
    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "Plotly Bar Chart":
    fig = px.bar(df.head(10), x="sepal length (cm)", y="petal length (cm)", color=df.target.map(lambda x: iris.target_names[x]))
    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "Plotly Scatter Plot":
    fig = px.scatter(df, x="sepal length (cm)", y="petal length (cm)", color=iris.target_names[df.target])
    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "Plotly Box Plot":
    fig = px.box(df, x=iris.target[df.index], y="sepal length (cm)", color=iris.target_names[df.target])
    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "Plotly Pie Chart":
    sample = df["target"].value_counts()
    fig = px.pie(values=sample, names=iris.target_names)
    st.plotly_chart(fig, use_container_width=True)

# =========================
# BOKEH CHARTS
# =========================
elif chart_type == "Bokeh Line Chart":
    p = figure(title="Bokeh Line Chart", width=700, height=400)
    p.line(df.index, df["sepal length (cm)"], line_width=2, color="green")
    st.bokeh_chart(p)

elif chart_type == "Bokeh Area Chart":
    x = df.index[:50]
    y = df["petal length (cm)"][:50]
    p = figure(title="Bokeh Area Chart", width=700, height=400)
    p.varea(x=x, y1=0, y2=y, fill_color="skyblue", alpha=0.6)
    st.bokeh_chart(p)


elif chart_type == "Bokeh Pie Chart":
    counts = df["target"].value_counts()
    pie_data = pd.Series(counts, index=iris.target_names).reset_index(name='value')
    pie_data.columns = ['species', 'value']
    pie_data['angle'] = pie_data['value'] / pie_data['value'].sum() * 2 * pi
    pie_data['color'] = Category10[len(pie_data)]

    source = ColumnDataSource(pie_data)

    p = figure(height=400, title="Bokeh Pie Chart", toolbar_location=None,
               tools="hover", tooltips="@species: @value", x_range=(-0.5, 1.0))
    
    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True),
            end_angle=cumsum('angle'),
            line_color="white", fill_color='color',
            legend_field='species', source=source)

    p.axis.visible = False
    p.grid.visible = False

    st.bokeh_chart(p)


elif chart_type == "Bokeh Histogram":
    hist_data = df["petal length (cm)"]
    hist, edges = np.histogram(hist_data, bins=20)
    p = figure(title="Bokeh Histogram", width=700, height=400)
    p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], fill_color="purple", alpha=0.7)
    st.bokeh_chart(p)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit, Plotly & Bokeh")
