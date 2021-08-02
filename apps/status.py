import streamlit as st
import pandas as pd
import os
from pathlib import Path
from joblib import load
import pickle
import numpy as np
import json
import time

with open("apps/states_dict.json") as f:
    state_cfg = json.loads(f.read())
    #print(city_cfg.keys())

with open("apps/category_encode.json") as f:
    cat_cfg = json.loads(f.read())
    #print(city_cfg.keys())

def app():
    
    ##file = 'apps/Cleaned_startup data [data15].csv'
    ##path_to_file = (os.path.join((Path.cwd()),file))
    #dataset = pd.read_csv(path_to_file)
    #dataset.head()
    
    Title = "Predict the Status of the Startup"
    Description=""
    st.title(Title)
    st.markdown(Description)

    @st.cache
    def load_data():
        data = pd.read_csv("apps/Cleaned_startup data [data15].csv")
        return data
    data = load_data()
    st.write(data)


    #@st.cache(allow_output_mutation=True)
    def load_model(path='models/status_sklearn_final_1.pkl'):
        model = pickle.load(open(path,'rb'))
        return model

    clf = load_model()
    if st.sidebar.checkbox("Predict Acquired or Closed", False):
        st.header("Predict if the startup will be Aquired or Closed based on these features")
        # Declare a form and call methods directly on the returned object
        f = st.form(key='ml_form')
        is_top500 = f.selectbox("Is one of the top 500 startups", [1,0]) 
        
        relationships = f.slider("Number of Relationships to stakeholders, investors",0,500)
        milestones = f.slider("No of Milestones acheived",0,10)
        #latitude = f.number_input(label='Latitude of the headquarters of the company')
        funding_total = f.slider("Funding Total (in million usd)",0,1000)
        funding_rounds = f.slider("Number of Funding Rounds",0,10)
        avg_participants = f.slider("Average number of Participants in the funding rounds",0,100)

        states_list = list(state_cfg.keys())
        print('len')
        print((states_list))
        state = str(f.selectbox("State Code",states_list))
        state_encode = state_cfg[state]

        categories_list = list(cat_cfg.keys())
        print('len2')
        print((categories_list))
        cat = str(f.selectbox("Category",categories_list))
        cat_encode = cat_cfg[cat]

        submitted = f.form_submit_button(label='Submit!')
        if submitted:

            with st.spinner("Predicting the Status of the Startup ......"):
                time.sleep(2)
                my_data = np.array([relationships,milestones,is_top500,funding_total*10000,avg_participants,funding_rounds,cat_encode,state_encode])
                #print(my_data)
                try:
                    prediction = clf.predict([my_data])

                    if prediction == 1:
                        st.markdown(""" ### Acquired! """)
                    else:
                        st.markdown(""" ### Closed!   """)

                    #print(clf.predict_proba([my_data]))
                    #result = round(prediction[0],2)

                    #st.markdown(""" ### Status : """ + str(result) + "%")

                    #st.write(prediction)
                except Exception as e:
                    f.error(f"Could not make prediction. {e}")
                

        