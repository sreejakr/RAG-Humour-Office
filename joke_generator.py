import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    raise ValueError(" Missing GOOGLE_API_KEY in .env file!")

llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    temperature=0.7,
    google_api_key=google_api_key
)

prompt = ChatPromptTemplate.from_template(
    "Create a joke in the style of Michael Scott from 'The Office' based on the following dialogues:\n\n"
    "{retrieved_context}\n\n"
    "User request: {user_query}\n\n"
    "Joke:"
)

llm_chain = prompt | llm

def generate_joke(retrieved_context, user_query):
    if not retrieved_context:
        retrieved_context = "I don't have any specific dialogues about this topic, but I'll still try to make a Michael Scott-style joke!"
    
    response = llm_chain.invoke({"retrieved_context": retrieved_context, "user_query": user_query})
    return response.get('text', str(response)) if isinstance(response, dict) else str(response)

if __name__ == "__main__":
    test_context = "Michael Scott once said: 'I'm not superstitious, but I am a little stitious.'"
    test_query = "Make a joke about beets."
    print("Generated Joke:", generate_joke(test_context, test_query))
