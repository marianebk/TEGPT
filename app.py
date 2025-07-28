import os
import streamlit as st
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from llama_index.llms.openai import OpenAI

# 🔧 Path to external USB drive data
EXTERNAL_DATA_DIR = "/Volumes/FOUNDERSBAY 1/data"
INDEX_DIR = "./storage"

# 🔐 Load OpenAI API key
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# 📋 Streamlit UI
st.set_page_config(page_title="TE GPT", layout="wide")
st.title("🤖 TE GPT Assistant")
st.write("Ask questions about your TE lighting and operations system.")

# 📚 Load or build the index
if not os.path.exists(INDEX_DIR):
    with st.spinner("Indexing files from USB drive... please wait."):
        documents = SimpleDirectoryReader(EXTERNAL_DATA_DIR).load_data()
        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist(persist_dir=INDEX_DIR)
else:
    storage_context = StorageContext.from_defaults(persist_dir=INDEX_DIR)
    index = load_index_from_storage(storage_context)

# 💬 Chat UI
query_engine = index.as_query_engine()
query = st.text_input("Ask me something:")
if query:
    with st.spinner("Thinking..."):
        response = query_engine.query(query)
        st.markdown("### 💬 Answer")
        st.markdown(response.response)
