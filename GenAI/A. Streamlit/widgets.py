import streamlit as st

st.title("Chai maker app")

if st.button("Make Chai"):
    st.success("Got it")

add_masala = st.checkbox("ADD")

if add_masala:
    st.write("You won")

tea_type = st.radio ("Pick base: " , ["Hello", "bye"])
st.write(f"Selected {tea_type} is great")

sugar = st.slider("sugar", 0, 5,2);
st.write(f"Selected sugar level {sugar}")

cups = st.number_input("How many cups", min_value=1, max_value=23)
st.write(f"You ordered {cups} of tea")

name = st.text_input("Enter your name")
if name:
    st.write(f"Welcome, {name} ! Your chai is on the way")

