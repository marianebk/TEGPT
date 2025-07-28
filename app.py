import os
import streamlit as st
from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext,
    load_index_from_storage,
    Settings,
)
from llama_index.llms.openai import OpenAI
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.prompts import PromptTemplate

# CONFIGURE YOUR OPENAI API KEY
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# Set LlamaIndex global settings
Settings.llm = OpenAI(model="gpt-4")
Settings.chunk_size = 512
Settings.chunk_overlap = 50

# Define paths
DATA_DIR = "./data"
INDEX_DIR = "./storage"

# Streamlit UI setup
st.set_page_config(page_title="🤖 TE GPT Assistant")
st.title("🤖 TE GPT Assistant")
st.markdown(
    "Ask detailed questions about your TE lighting and operations system. "
    "Responses will include clear explanations and step-by-step instructions where appropriate."
)

# Check or build index
if not os.path.exists(INDEX_DIR):
    st.info("Indexing files from USB drive... please wait ⏳")
    if not os.path.exists(DATA_DIR):
        st.error(f"Directory {DATA_DIR} not found.")
        st.stop()

    documents = SimpleDirectoryReader(DATA_DIR).load_data()
    parser = SentenceSplitter(chunk_size=512, chunk_overlap=50)
    index = VectorStoreIndex.from_documents(documents, transformations=[parser])
    index.storage_context.persist(persist_dir=INDEX_DIR)
else:
    storage_context = StorageContext.from_defaults(persist_dir=INDEX_DIR)
    index = load_index_from_storage(storage_context)

# Custom verbose response prompt
prompt = PromptTemplate(
    "You are a TE systems assistant specialized in lighting, front-of-house tech, and operations. "
    "When responding to user questions, provide as much relevant detail as possible. Break complex processes into clear, step-by-step instructions. "
    "If appropriate, explain why certain steps matter or what tools are typically involved. Be concise but thorough.\n\n"
    "Please cite any references and where they came from in the information we've uploaded. Put it in quotation marks and make it a link to the document it was taken from"
    "User question: {query_str}\n\n"
    "Detailed answer:"
)

# Set up query engine
query_engine = index.as_query_engine(text_qa_template=prompt)

# Ask the assistant
query = st.text_input("Ask me something:")
if query:
    response = query_engine.query(query)
    st.markdown("### Detailed Response:")
    st.write(response.response)
