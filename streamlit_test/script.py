import streamlit as st
import requests

api='http://localhost:8080/?coin-'

st.markdown('# Display value of crypto')

coin = st.text_input('What coin would you like to use?')

st.write("HOLA")

