import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
     # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    
import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos (ajusta la ruta a tu archivo CSV)
df = pd.read_csv("ruta/del/archivo.csv")  # Cambia esto por la ruta correcta

# Encabezado
st.header("Visualización de Datos con Streamlit y Plotly")

# Botón para mostrar un histograma
if st.button("Mostrar Histograma"):
    fig_hist = px.histogram(df, x="columna_x")  # Reemplaza con la columna correcta
    st.plotly_chart(fig_hist)

# Botón para mostrar un gráfico de dispersión
if st.button("Mostrar Gráfico de Dispersión"):
    fig_scatter = px.scatter(df, x="columna_x", y="columna_y")  # Reemplaza con las columnas correctas
    st.plotly_chart(fig_scatter)
    
import streamlit as st
import pandas as pd
import plotly.express as px

# Crear datos de ejemplo
df = pd.DataFrame({
    "x": [1, 2, 3, 4, 5],
    "y": [10, 20, 15, 30, 25]
})

# Botón para mostrar gráfico de dispersión
if st.button("Mostrar gráfico de dispersión"):
    st.write("Aquí tienes un gráfico de dispersión:")
    fig = px.scatter(df, x="x", y="y", title="Gráfico de Dispersión")
    st.plotly_chart(fig)


