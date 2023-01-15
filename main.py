import streamlit as st


col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")
    
with col2:
        st.title("Alex  Vic")
        content = """Hey! , i am Alex a Python programmer from israel
        """
        st.info(content)
        
content2 = """
Below you can find some of the app i have built in Python. Feel free to contact me.!"""  

st.write(content2)    