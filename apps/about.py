import os
import streamlit as st
#import streamlit.components.v1 as components
from streamlit_lottie import st_lottie
import requests
import json
import time

def read_markdown(path,parent='about/'):
    with open(os.path.join(parent,path)) as f:
        return f.read()

#@st.cache
def load_lottie_json(path='images/startups.json'):
    f = open(path)
    lottie_json = json.load(f)
    return lottie_json

@st.cache
def load_dataviz(path='images/eda.html'):
    with open(path) as f:
        eda = f.read()
        return eda
    
def app():
    
    st.markdown(read_markdown("intro.md"))
    st_lottie(load_lottie_json())    
    st.markdown(read_markdown("problemstatement.md"))
    #st.image('images/taskflow.png')
    #st.markdown(read_markdown("task1.md"))
    #st.markdown(read_markdown("task2.md"))
    #st.markdown(read_markdown("task3.md"))
    st.markdown(read_markdown("task4.md"))
    st.components.v1.html(load_dataviz(),height = 800,width = 800)
    #st.markdown(read_markdown("task5.md"))
    #st.markdown(read_markdown("task6.md"))
    #st.markdown(read_markdown("task7.md"))
    #st.markdown(read_markdown("futurework.md"))
    st.markdown(read_markdown("credits.md"))
    st.markdown("![Omdena](https://omdena.com/wp-content/uploads/2019/12/logo-2.png)")
    #st.markdown("![Omdena Penn Chapter](https://omdena.com/wp-content/uploads/2021/06/4.png:small)")


     
    
    