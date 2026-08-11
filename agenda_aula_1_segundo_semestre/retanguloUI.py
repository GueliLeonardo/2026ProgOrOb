import streamlit as st
from retangulo import Retangulo

class RetanguloUI:
    def main():
        st.header("Cálculos com retângulo")
        b = st.text_input("informe Base")
        h = st.text_input("informe Altura")
        if st.button("Calcular"):
            r = Retangulo(float (b), float (h))
            st.write(f"Área = {r.calc_area():.2f}")
            st.write(f"Diagonal = {r.calc_diagonal():.2f}")
            st.write(r)
