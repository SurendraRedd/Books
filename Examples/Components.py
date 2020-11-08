import streamlit as st

st.sidebar.subheader("Component 1")

t1 = st.sidebar.text_input("Component 1 name")
s1 = st.sidebar.slider("Component 1 value")

st.sidebar.markdown("---")

st.sidebar.subheader("Component 2")
t2 = st.sidebar.text_input("Component 2 name")
s2 = st.sidebar.slider("Component 2")

st.title("Hello!")

st.write(t1, s1)
st.write(t2, s2)
