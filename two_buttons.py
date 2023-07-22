import streamlit as st 

st.write('''Buttons will not hold state. 
         After clicking the second button, the state of button One will revert back to False.
         Action from button One will be errased. And Vice Versa
         
         This illustrates an anti pattern''')

if st.button('One', key="btn_one"):
    st.write('One')

if st.button('Two', key="btn_two"):
    st.write('Two')