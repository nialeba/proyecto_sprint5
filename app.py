import pandas as pd 
import streamlit as st
import plotly.express as px
import numpy as np
import plotly.graph_objects as go

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
st.header('Análisis exploratorio de datos de automóviles en venta')
st.write('¡Bienvenid@!')
st.write('En esta página, con tan solo un par de clicks, podrás conocer y analizar un poco más las características de los automóviles listados para su venta durante el periodo 2018-2019.')

st.write('Antes que nada, vámos a visualizar los datos de los vehículos de acuerdo a sus características. Marca la siguiente casilla para observarlos.')
if st.checkbox('Visualiza los datos'): # crear una casilla de selección
    show_data = car_data.head(10)
    show_data

st.write('No olvides que puedes hacer "click" en cada uno de los títulos de las columnas para ordenar las características de los automóviles en venta.')

st.write('Ahora vámos a construir algunos gráficos de barra con los datos que observamos anteriormente. Da "click" en el siguiente botón para desplegar algunos gráficos predeterminados.')

bar_button = st.button('Construir gráficos de barra') # crear un botón
        
if bar_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('¡Listo! En esta sección podrás analizar el número de vehículos listados para su venta, de acuerdo a su condición, la empresa que lo manufacturó y su tipo.') 
    st.write('Recuerda que las gráficas son interactivas y puedes activar y desactivar una o más de las etiquetas de la leyenda de cada gráfica, ¡no dudes en inténtarlo!')
    # escribir función para seleccionar la empresa manufacturera del modelo
    def manufacturer(model):
        result= model.split(' ')[0][:]
        return result
    # aplicar función sobre la columna del modelo
    car_data['manufacturer']=car_data['model'].apply(manufacturer)
    # crear un gráfico de barra de empresa manufacturera vs condición
    fig = px.bar(car_data, x='manufacturer', color='condition')
    # modificar las características del gráfico
    fig.update_layout(
        title='Número de vehículos por empresa manufacturera y condición',
        xaxis_title= 'Empresa manufacturera',
        yaxis_title= 'Número de vehículos'
    )
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    # crear un gráfico de barra de empresa manufacturera vs tipo
    fig1 = px.bar(car_data, x='manufacturer', color='type')
    # modificar las características del gráfico
    fig1.update_layout(
        title='Número de vehículos por empresa manufacturera y tipo',
        xaxis_title= 'Empresa manufacturera',
        yaxis_title= 'Número de vehículos'
    )
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig1, use_container_width=True)
    # crear un gráfico de barra condición vs transmisión
    fig2 = px.bar(car_data, x='condition', color='transmission')
    # modificar las características del gráfico
    fig2.update_layout(
        title='Número de vehículos por su condición y tipo de transmisión',
        xaxis_title= 'Condición del vehículo',
        yaxis_title= 'Número de vehículos'
    )
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)

st.write('A continuación, vámos a construir un histograma para analizar el número de vehículos según el año de su modelo y su condición. Para ello da "click" en el boton de abajo.')

hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón

    # crear un histograma
    fig3 = px.histogram(car_data, x="model_year", color='condition')
    # modificar las características del gráfico
    fig3.update_layout(
        title='Número de vehículos por año del modelo y condición',
        xaxis_title= 'Año del modelo',
        yaxis_title= 'Número de vehículos'
    )
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig3, use_container_width=True)
    # escribir un mensaje
    st.write('¡Genial! En este histograma incluso podemos observar el impacto de la crisis financiera del 2008 en la venta de vehículos. Observa el abrupto descenso en el número de vehículos listados en el año 2009 independientemente de su condición.') 

st.write('Para proseguir con el análisis vámos a construir un gráfico de dispersión entre el precio de los vehículos y los kilómetros acumulados que marca su odómetro ¿Será que entre mayor el número de kilómetros, menor su precio? ¡Veámos!.')
st.write('Da "click" en el siguiente botón para desplegar el gráfico.')

scatter_button = st.button('Construir gráfica de dispersión') # crear un botón
        
if scatter_button: # al hacer clic en el botón
    # convertir la fecha de publicación a tipo datatime
    car_data['date_posted'] = pd.to_datetime(car_data['date_posted'], format= '%d/%m/%Y')
    # crear una variable con el año de publicación
    car_data['year_posted'] = car_data['date_posted'].dt.year
    car_data['year_posted'] = car_data['year_posted'].astype(str)
    # crear el gráfico de dispersión
    fig4 = px.scatter(car_data, x="odometer", y="price", color='year_posted', title='Relación entre el precio del vehículo y medición de odómetro por año')
    # modificar las características del gráfico
    fig4.update_layout(
        title='Relación entre el precio del vehículo y medición de odómetro por año',
        xaxis_title= 'Odómetro (km)',
        yaxis_title= 'Precio (dólares)'
    )
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig4, use_container_width=True)
    st.write('Mmm...al parecer sí, pero no queda completamente claro, sin duda se requiere de algunas pruebas estadísticas extras para llegar a una conclusión precisa.')

st.subheader('Comparación de la distribución de precios entre empresas manufactureras')
st.write('En esta sección podrás comparar los precios de los vehículos listados de acuerdo a la empresa que los manufacturó. Selecciona en los dos menús de abajo las empresas que desees comparar.')
option1 = st.selectbox(
    "Selecciona la empresa manufacturera 1",
    ('bmw', 'ford', 'hyundai', 'chrysler', 'toyota', 'honda', 'kia', 'chevrolet',
     'ram', 'gmc', 'jeep', 'nissan', 'subaru', 'dodge', 'mercedes-benz', 'acura',
     'cadillac', 'volkswagen', 'buick')
     )

st.write("Seleccionaste:", option1)

option2 = st.selectbox(
    "Selecciona la empresa manufacturera 2",
    ('bmw', 'ford', 'hyundai', 'chrysler', 'toyota', 'honda', 'kia', 'chevrolet',
     'ram', 'gmc', 'jeep', 'nissan', 'subaru', 'dodge', 'mercedes-benz', 'acura',
     'cadillac', 'volkswagen', 'buick')
     )

st.write("Seleccionaste:", option2)

comp_button = st.button('Visualizar histograma normalizado') # crear un botón
        
if comp_button: # al hacer clic en el botón

    def manufacturer(model):
        result= model.split(' ')[0][:]
        return result
    # aplicar función sobre la columna del modelo
    car_data['manufacturer']=car_data['model'].apply(manufacturer)
    price_1 = car_data[car_data['manufacturer']==option1].loc[:,['price','manufacturer']]
    price_2 = car_data[car_data['manufacturer']==option2].loc[:,['price','manufacturer']]
    df_price = pd.concat([price_1, price_2])
    fig6 = px.histogram(df_price, x="price", color='manufacturer', histnorm='probability') 
    fig6.update_traces(opacity=0.75)
    fig6.update_layout(
        title='Histograma de precio vs empresa manufacturera',
        xaxis_title= 'Precio',
        yaxis_title= 'Probabilidad'
        )
    st.plotly_chart(fig6, use_container_width=True)
    
st.write('!Muy bien🎉! Hasta aquí hemos llegado, espero que los gráficos que has construido te hayan servido para profundizar tus conocimientos sobre los vehículos listados para su venta entre los años 2018 y 2019.')
