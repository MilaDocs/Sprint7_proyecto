import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la aplicación
st.title("Análisis de vehículos en venta")

# Carga de datos
df = pd.read_csv("vehicles_us.csv")

# Muestra los primeros registros del DataFrame
st.write("Vista previa de los datos:", df.head())

# Histograma
if st.button("Mostrar histograma"):
    fig_hist = px.histogram(df, x="price", title="Distribución de Precios")
    st.plotly_chart(fig_hist)

# Gráfico de dispersión
if st.button("Mostrar gráfico de dispersión"):
    fig_scatter = px.scatter(df, x="odometer", y="price", title="Relación entre Kilometraje y Precio")
    st.plotly_chart(fig_scatter)
