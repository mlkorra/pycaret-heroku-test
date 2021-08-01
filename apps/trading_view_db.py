from json import load
import streamlit as st
import streamlit.components.v1 as components


def load_dataviz(path='./images/databoard.html'):
    with st.spinner("Loading the Dashboard......"):
        with open(path) as f:
            trading_view_db = f.read()
            check = 0
            return trading_view_db

def app():
    
    st.title("TradingView Dashboard")
    
    components.html(load_dataviz(),height = 600,width = 1600)
    
    st.text(" \n \n ")
    st.write("For more details on how to copy the dashboard,you can check the About section!") 