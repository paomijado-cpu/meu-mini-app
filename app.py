import streamlit as st

st.title("Mini App Interativo")
nome = st.text_input("Qual é o seu nome?")
if st.button("Enviar"):
    st.success(f"Olá, {nome}! Bem-vindo ao Streamlit! 🚀")