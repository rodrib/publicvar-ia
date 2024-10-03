import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Cargar tu dataset
# Reemplaza 'ruta/del/tu/dataset.csv' con la ruta correcta de tu archivo CSV
df = pd.read_csv('data_cancer.csv')

# Eliminar filas con NaN en la columna 'HC'
df = df.dropna(subset=['HC'])

# Función para calcular la similitud del coseno entre dos textos
def calculate_cosine_similarity(text1, text2):
    vectorizer = CountVectorizer().fit_transform([text1, text2])
    vectors = vectorizer.toarray()
    similarity = cosine_similarity([vectors[0]], [vectors[1]])
    return similarity[0][0]

# Página principal de Streamlit
def main():
    st.title("Similitud de Historias Clínicas (HC)")

    with st.expander('Sobre esta app'):
        st.markdown('**¿Qué puede hacer esta aplicación??**')
        st.info('Esta aplicación muestra la similitud de HC utilizando diversas metricas como en este caso la distancia del coseno')
        st.markdown('**How to use the app?**')
        st.warning('Para interactuar con la aplicación, 1. Ingrese un ID del paciente')

    # Sidebar con entrada de usuario
    patient_id = st.sidebar.text_input("Ingrese el ID del paciente:", "")
    submit_button = st.sidebar.button("Buscar")

    if submit_button and patient_id:
        # Validar si el ID es un número entero y existe en el DataFrame
        if patient_id.isdigit() and int(patient_id) in df['ID'].values:
            # Acceder a los datos del paciente
            patient_data = df[df['ID'] == int(patient_id)].iloc[0]

            # Calcular la similitud del coseno entre la HC del paciente y otros pacientes (excluyendo al mismo paciente)
            similarities = df[df['ID'] != int(patient_id)]['HC'].apply(lambda x: calculate_cosine_similarity(patient_data['HC'], x))
            most_similar_patient_id = similarities.idxmax()
            most_similar_patient_data = df.loc[most_similar_patient_id]

            # Mostrar resultados
            st.subheader(f"Historia Clínica del Paciente {patient_id}:")
            st.write(patient_data['HC'])

            st.subheader(f"Paciente más similar (ID {most_similar_patient_id}):")
            st.write(most_similar_patient_data['HC'])
            st.write(f"Similitud del coseno: {similarities[most_similar_patient_id]:.2f}")

        else:
            st.warning("Ingrese un ID válido.")

# Ejecutar la aplicación
if __name__ == "__main__":
    main()