import streamlit as st
from retrieval import retrieve_dialogues
from joke_generator import generate_joke
import os
import torch

# Fix for Torch's dynamic class resolution in Streamlit
torch.classes.__path__ = []  

st.set_page_config(page_title="Michael Scott Joke Generator", page_icon="😂", layout="centered")

st.title("Michael Scott Joke Generator")
st.write("Enter a topic to get a joke in the style of Michael Scott from *The Office*!")

user_query = st.text_input("Enter a topic (e.g., sales, beets, relationships)", "")

# Use session state to store retrieval and joke generation results
if "retrieved_text" not in st.session_state:
    st.session_state.retrieved_text = None

if "generated_joke" not in st.session_state:
    st.session_state.generated_joke = None

if st.button("Generate Joke"):
    if user_query:
        if not st.session_state.retrieved_text:  # Run retrieval only if not already done
            with st.spinner("Retrieving dialogues..."):
                st.session_state.retrieved_text = retrieve_dialogues(user_query)
                print(f"✅ Retrieved Text: {st.session_state.retrieved_text}")

        if not st.session_state.retrieved_text.strip():
            st.error("No relevant dialogues found. Try a different topic!")
        else:
            if not st.session_state.generated_joke:  # Run joke generation only if not already done
                with st.spinner("Generating your joke..."):
                    st.session_state.generated_joke = generate_joke(st.session_state.retrieved_text, user_query)
                    print(f"✅ Generated Joke: {st.session_state.generated_joke}")

            st.subheader("Here's your joke:")
            st.write(st.session_state.generated_joke)

    else:
        st.warning("Please enter a topic before generating a joke!")
