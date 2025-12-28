import pandas as pd
import streamlit as st
from fetchdata import df
import plotly.express as px




st.title('UK Electricity Generation Mix Visualization')
@st.cache_data
def get_data():
    return df.copy()

data = get_data()

# --- All generation graph ---
st.subheader("Generation Mix Over Time")
fuel_columns = [col for col in df.columns if col != 'time']
selected_fuels = st.multiselect("Select fuels to display", fuel_columns, default=fuel_columns)

fig1 = px.line(
    data,
    x='time',
    y=selected_fuels,
    title="UK Electricity Generation Mix"
)
fig1.update_yaxes(range=[0, 100], title_text="Percentage (%)")
st.plotly_chart(fig1, width='stretch')


# --- Renewable vs non-renewable graph ---
st.subheader("Renewable vs. Non-Renewable Generation")
renewable_cols = ['solar', 'wind', 'hydro']
non_renewable_cols = [col for col in df.columns if col not in renewable_cols + ['time']]

data['Renewables'] = data[renewable_cols].sum(axis=1)
data['Non_Renewables'] = data[non_renewable_cols].sum(axis=1)

fig2 = px.line(
    data,
    x='time',
    y=['Renewables', 'Non_Renewables'],
    title="Renewable vs Non-Renewable Electricity Generation",
    labels={'value': 'Percentage (%)', 'variable': 'Source'}
)
fig2.update_yaxes(range=[0, 100])
st.plotly_chart(fig2, width='stretch')

# --- Show raw data ---
st.subheader("Raw Data")
st.dataframe(data)  # scrollable table
