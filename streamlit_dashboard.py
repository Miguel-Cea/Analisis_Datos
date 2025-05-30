
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Título de la aplicación
st.title('Análisis Interactivo de Datos - DATOS_INFORME_GALA_CLEANED 1.xlsx')

# Cargar el archivo Excel
uploaded_file = st.file_uploader("Carga el archivo DATOS_INFORME_GALA_CLEANED 1.xlsx", type=["xlsx"])

if uploaded_file:
    # Leer el archivo Excel
    df = pd.read_excel(uploaded_file, engine='openpyxl')

    # Seleccionar columnas para análisis
    columns_to_analyze = st.multiselect(
        "Selecciona las columnas para análisis",
        df.columns.tolist(),
        default=df.columns.tolist()
    )

    # Función para crear gráficos
    def create_charts(column_name):
        safe_column_name = column_name.replace("/", "_").replace(" ", "_").strip()

        # Gráfico de barras
        plt.figure(figsize=(10, 6))
        df[column_name].value_counts().plot(kind='bar')
        plt.title(f'Distribución de {column_name}')
        plt.xlabel(column_name)
        plt.ylabel('Frecuencia')
        st.pyplot(plt)

        # Nube de palabras
        text = ' '.join(df[column_name].dropna().astype(str).tolist())
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(f'Nube de palabras de {column_name}')
        st.pyplot(plt)

    # Generar gráficos y mostrar en la aplicación
    for column in columns_to_analyze:
        st.header(column)
        create_charts(column)
        st.subheader('Conclusiones')
        st.write(f'Conclusiones del análisis de la columna {column}.')
