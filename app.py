import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn import datasets
from bokeh.plotting import figure
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash import Input, Output
from streamlit.components.v1 import html

# Load Iris dataset
iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Streamlit Page Configuration
st.set_page_config(page_title="Multi Chart Showcase", page_icon="📊", layout="wide")

# Title
st.title("Interactive Charts Showcase")
st.header("Displaying various charts using Plotly, Bokeh, and Dash")

# Plotly Line Chart
st.subheader("Plotly Line Chart")
fig = px.line(df, x="sepal length (cm)", y="sepal width (cm)", color="species")
st.plotly_chart(fig)

# Bokeh Scatter Plot
st.subheader("Bokeh Scatter Plot")
p = figure(title="Bokeh Scatter Plot", x_axis_label='Sepal Length (cm)', y_axis_label='Sepal Width (cm)')
p.scatter(df["sepal length (cm)"], df["sepal width (cm)"], legend_field="species", size=8, color="red", alpha=0.5)
st.bokeh_chart(p)

# Dash App Integration
st.subheader("Dash Interactive Plot")

# Start a Dash app inside Streamlit
app = dash.Dash(__name__)

# Define the layout of the Dash app
app.layout = html.Div([
    html.H1("Dash Plot: Sepal Length vs Sepal Width"),
    dcc.Graph(
        id='scatter-plot',
        figure=go.Figure(
            data=[go.Scatter(
                x=df['sepal length (cm)'],
                y=df['sepal width (cm)'],
                mode='markers',
                marker=dict(color='blue'),
                text=df['species']
            )],
            layout=go.Layout(
                title="Dash Plot of Iris Dataset",
                xaxis=dict(title="Sepal Length (cm)"),
                yaxis=dict(title="Sepal Width (cm)")
            )
        )
    )
])

# Run Dash App in the background and embed it within the Streamlit app
def run_dash():
    app.run_server(debug=False, use_reloader=False, port=8051)

# Using Streamlit component to run the Dash app in the background
html("<div id='dash-container'></div><script src='http://127.0.0.1:8051'></script>")

# Footer Information
st.markdown("---")
st.markdown("For more charts and visualizations, feel free to explore Streamlit, Plotly, Bokeh, and Dash documentation!")
