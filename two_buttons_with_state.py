import streamlit as st 

st.write('''Persisting the results of multiple users interactions
         To achieve this, use session state
         
         Notice button two has no session state and its value will dissaper on rerun''')

# Introduce a variable in session_state
if 'btn_one_clicked' not in st.session_state:
    st.session_state.btn_one_clicked = False

def click_button_one():
    st.session_state.btn_one_clicked = True

st.button('One', key="btn_one", on_click=click_button_one)

if st.session_state.btn_one_clicked:
    st.write('Button clicked!')
    st.slider('Select a value')

if st.button('Two', key="btn_two"):
    st.write('Two')