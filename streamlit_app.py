import streamlit as st

st.title("Hello World")
name = st.text_input("Masukan nama anda :")
if name :
    st.write(f"halo {name}, apakabar ?")
else:
    st.warning("masukan nama anda !")
