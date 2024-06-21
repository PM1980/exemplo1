import streamlit as st

st.title("Calculadora de Soma")

# Criar campos de entrada para os dois números
num1 = st.number_input("Insira o primeiro número:", value=0.0)
num2 = st.number_input("Insira o segundo número:", value=0.0)

# Calcular a soma
soma = num1 + num2

# Exibir o resultado em uma caixa
st.text_input("A soma é:", value=str(soma), disabled=True)
