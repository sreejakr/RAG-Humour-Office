import streamlit as st
from retrieval import retrieve_dialogues
from joke_generator import generate_joke

st.set_page_config(page_title="Michael Scott Joke Generator", page_icon="😂", layout="centered")

st.title("Michael Scott Joke Generator")
st.write("Enter a topic, and get a joke in the style of Michael Scott from *The Office*!")

user_query = st.text_input("Enter a topic (e.g., sales, beets, relationships)", "")

if st.button("Generate Joke"):
    if user_query:
        with st.spinner("Retrieving dialogues..."):
            retrieved_text = retrieve_dialogues(user_query)

        with st.spinner("Generating your joke..."):
            response = generate_joke(retrieved_text, user_query)

        st.subheader("Here's your joke:")
        st.write(response)
    else:
        st.warning("Please enter a topic before generating a joke!")
