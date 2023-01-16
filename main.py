import streamlit as st
import pandas

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

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])  
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

                 