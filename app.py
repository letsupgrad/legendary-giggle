import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go # Use graph_objects for more control if needed
from sklearn import datasets
from bokeh.plotting import figure, show
from bokeh.palettes import Category10 # For distinct colors
from bokeh.transform import factor_cmap

# Load Iris dataset
iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
species_list = df['species'].unique().tolist()

# Streamlit Page Configuration
st.set_page_config(page_title="Multi Chart Showcase", page_icon="📊", layout="wide")

# Title
st.title("Interactive Charts Showcase")
st.header("Displaying various charts using Plotly and Bokeh")

# --- Plotly Line Chart ---
st.subheader("Plotly Line Chart (Example)")
st.markdown("Plotting Sepal Length vs Sepal Width, colored by species.")
# Ensure data is sorted if a meaningful line plot is desired, otherwise it connects points in order
df_sorted = df.sort_values(by=["species", "sepal length (cm)"])
fig_line = px.line(df_sorted, x="sepal length (cm)", y="sepal width (cm)", color="species",
                   title="Plotly Line: Sepal Length vs. Sepal Width")
st.plotly_chart(fig_line, use_container_width=True)


# --- Bokeh Scatter Plot ---
st.subheader("Bokeh Scatter Plot")
st.markdown("Plotting Sepal Length vs Sepal Width, colored by species with interactive tools.")

# Create a color map for species
color_map = factor_cmap('species', palette=Category10[len(species_list)], factors=species_list)

p = figure(title="Bokeh Scatter: Sepal Length vs Sepal Width",
           x_axis_label='Sepal Length (cm)',
           y_axis_label='Sepal Width (cm)',
           height=400,  # Adjust size as needed
           tools="pan,wheel_zoom,box_zoom,reset,hover,save") # Add hover tool

# Add glyphs
p.scatter(x="sepal length (cm)",
          y="sepal width (cm)",
          source=df,
          legend_field="species", # Correctly use legend_field with source=df
          fill_alpha=0.6,
          size=10,
          color=color_map) # Apply the color map

# Customize legend
p.legend.location = "top_left"
p.legend.title = "Species"
p.legend.click_policy="hide" # Allow hiding species by clicking legend

st.bokeh_chart(p, use_container_width=True)


# --- Plotly Interactive Scatter Plot (Replaces Dash) ---
st.subheader("Plotly Interactive Scatter Plot")
st.markdown("Plotting Sepal Length vs Sepal Width, colored by species (similar to the Dash example).")

fig_scatter = px.scatter(df, x="sepal length (cm)", y="sepal width (cm)", color="species",
                         title="Plotly Scatter: Sepal Length vs. Sepal Width",
                         hover_data=['petal length (cm)', 'petal width (cm)']) # Add more data on hover

# Update layout for better appearance if desired
fig_scatter.update_layout(
    xaxis_title="Sepal Length (cm)",
    yaxis_title="Sepal Width (cm)",
    legend_title="Species"
)
st.plotly_chart(fig_scatter, use_container_width=True)


# Footer Information
st.markdown("---")
st.markdown("Explore Streamlit, Plotly, and Bokeh documentation for more chart types and customization options!")
