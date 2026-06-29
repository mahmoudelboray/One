
import streamlit as st
import pandas as pd
import pickle

st.title("DKHousing Price Prediction App")

st.write(
    '''
This App classifies Families into 3 classes based on their Family Class.
''')

st.write(''' ## Classification of Families based on Family Class:
* **High Class Family**: (Rich Customers) , Purchase Price (>2500000) , High class House type , Wide Units
* **Middle Class Family**: (Middle Class Customers) , Purchase Price (>= 1000000) , Middle Class House type , Middle Units 
* **Low Class Family**: (Low Class Customers) , Purchase Price (< 1000000) , Low Class House type , Narrow Units
''')

st.image("https://medium.com/@realjema/the-end-of-social-classes-3d1b77aa37ea", width=700)

Purchase_Price = st.slider('Expected Purchase Price' , 500000 , 1000000 , 1500000, 2000000, 2500000, 3000000)
House_Type = st.slider('House Type' , 'High class Type' ,'Middle class Type' , 'Low class Type')
House_Size = st.slider('House Size' ,'Wide Units', 'Middle Units' , 'Narrow Units')




