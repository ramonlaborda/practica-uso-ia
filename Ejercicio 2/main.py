import streamlit as st
from function import initialize_openai, generate_post

# Configura la clave de la API de OpenAI
st.set_page_config(page_title="Chatbot Generador de Posts", layout="centered")
st.title("🗨 🚀 Chatbot para Generar Posts de LinkedIn")

# Entrada de clave API (puedes usar secretos de Streamlit para más seguridad)
api_key = st.secrets["openai"]["api_key"]

if api_key:
    initialize_openai(api_key)

    # Opciones de tipo de post
    tipo_post = ["Informativo", "Buscamos Trabajador (Contratacion)", "Newsletter"]
    context = st.text_area("Escribe el tema del post:")
    selected_tp = st.selectbox("Selecciona el tipo de post:", tipo_post)

    # Botón para generar post
    if st.button("Generar Post"):
        if context and selected_tp:
            with st.spinner("Generando tu post..."):
                post = generate_post(context, selected_tp)
            st.success("¡Post generado!")
            st.write(post)
        else:
            st.error("Por favor, completa todos los campos antes de generar el post.")