import streamlit as st
from src.component.header import header_home
from src.component.footer import footer_home
from src.ui.base_layout import style_base_layout , style_background_home
def home_screen():
    
    
    
    header_home()
    style_background_home()
    style_base_layout()
    
    
    
    
    col1,col2=st.columns(2,gap="large")
    
    
    with col1:
        st.header("I'am Student ")
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135755.png", width=90)
        
        if st.button("Student portal",type='primary',icon=":material/arrow_outward:",icon_position="right"):
            st.session_state['login_type']='Student'
            st.rerun()
        
        
        
    with col2:
        st.header("I'am Teacher ")
        st.image("https://cdn-icons-png.flaticon.com/512/2784/2784445.png", width=90)
        if st.button("Teacher portal",type='primary',icon=":material/arrow_outward:",icon_position="right"):
            st.session_state['login_type']='Teacher'
            st.rerun()
    footer_home()
