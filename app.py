import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn import datasets
from bokeh.plotting import figure
from bokeh.io import output_file, show
import dash
import dash_core_components as dcc
import dash_html_components as html

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

# Dash Integration (in Streamlit)
st.subheader("Dash Interactive Plot")
# Start a Dash app inside Streamlit
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Dash Plot: Sepal Length vs Sepal Width"),
    dcc.Graph(
        id='scatter-plot',
        figure=px.scatter(df, x="sepal length (cm)", y="sepal width (cm)", color="species").update_layout(title="Dash Plot of Iris Dataset")
    )
])

# Run Dash app using Streamlit components
from streamlit.components.v1 import html
app.run_server(debug=False, use_reloader=False)

# Display Button to reload Streamlit app
st.write("Click to reload the Streamlit App")
if st.button("Reload"):
    st.experimental_rerun()

# Footer Information
st.markdown("---")
st.markdown("For more charts and visualizations, feel free to explore Streamlit, Plotly, Bokeh, and Dash documentation!")
