from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

# Load Gemini Pro LLM
llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7)

prompt = ChatPromptTemplate.from_template(
    "Create a joke in the style of Michael Scott from 'The Office' based on the following dialogues:\n\n"
    "{retrieved_context}\n\n"
    "User request: {user_query}\n\n"
    "Joke:"
)

llm_chain = LLMChain(llm=llm, prompt=prompt)

def generate_joke(retrieved_context, user_query):
    return llm_chain.invoke({"retrieved_context": retrieved_context, "user_query": user_query})
