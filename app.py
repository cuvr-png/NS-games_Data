import pandas as pd
import plotly.express as px
import streamlit as st

# Título y encabezado de la aplicación
st.set_page_config(page_title="Nintendo Switch Games Analysis", layout="wide")

st.header('🎮 Análisis Exploratorio de Juegos de Nintendo Switch')
st.write('Esta aplicación permite explorar calificaciones y ventas de los juegos de Nintendo Switch utilizando gráficos interactivos creados con Plotly Express.')

# Carga de datos
@st.cache_data
def load_data():
    df = pd.read_csv('Nintendo Switch Games.csv', encoding='latin1')
    df['Game'] = df['Game'].str.replace(r'\r?\nRead the review', '', regex=True)
    df['Total_Shipped_M'] = df['Total Shipped'].str.replace('m', '', case=False).astype(float)
    return df

df = load_data()

# Vista previa de los datos
if st.checkbox('Mostrar vista previa de los datos'):
    st.subheader('Muestra del conjunto de datos')
    st.dataframe(df[['Game', 'Publisher', 'Developer', 'Critic Score', 'User Score', 'Total_Shipped_M']].head(10))

st.subheader('Visualizaciones Interactivas')

# Componentes interactivos mediante casillas de verificación
build_histogram = st.checkbox('Construir histograma de Puntajes de la Crítica (Critic Score)')

if build_histogram:
    st.write('### Distribución de las calificaciones de la crítica')
    fig_hist = px.histogram(
        df, 
        x='Critic Score', 
        nbins=20, 
        title='Distribución de Critic Score',
        color_discrete_sequence=['#e60012']
    )
    st.plotly_chart(fig_hist, use_container_width=True)

build_scatter_scores = st.checkbox('Construir gráfico de dispersión: Critic Score vs User Score')

if build_scatter_scores:
    st.write('### Relación entre notas de la crítica y de los usuarios')
    fig_scatter1 = px.scatter(
        df.dropna(subset=['Critic Score', 'User Score']), 
        x='Critic Score', 
        y='User Score', 
        hover_name='Game',
        hover_data=['Publisher'],
        title='Critic Score vs User Score'
    )
    st.plotly_chart(fig_scatter1, use_container_width=True)

build_scatter_sales = st.checkbox('Construir gráfico de dispersión: Critic Score vs Ventas Totales (Millones)')

if build_scatter_sales:
    st.write('### Relación entre calificación de la crítica y unidades vendidas/distribuidas')
    fig_scatter2 = px.scatter(
        df.dropna(subset=['Critic Score', 'Total_Shipped_M']), 
        x='Critic Score', 
        y='Total_Shipped_M', 
        hover_name='Game',
        hover_data=['Publisher'],
        title='Critic Score vs Ventas Totales (en millones de copias)'
    )
    st.plotly_chart(fig_scatter2, use_container_width=True)
