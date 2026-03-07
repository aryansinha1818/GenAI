import streamlit as st

st.title("Hello Chai App")
st.subheader("Brewed with streamlit")
st.text("Welcome to your first iteractive app")
st.write("Choose your fav variety of chai")

chai = st.selectbox("Your fav chai: ", ["masala chai", "Kesar chai", "adrak chai"])
st.write(f"You choose {chai}. Excellent choice")
st.success("Well done")