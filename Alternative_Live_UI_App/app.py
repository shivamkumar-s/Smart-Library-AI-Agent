import streamlit as st
import pandas as pd
import google.generativeai as genai
import os

st.set_page_config(page_title="Smart Library AI Agent", page_icon="📚", layout="centered", initial_sidebar_state="expanded")

with st.sidebar:
    st.title("⚙️ System Control")
    st.markdown("---")
    st.markdown("** Internship:** AICTE & IBM SkillsBuild")
    st.markdown("---")
    st.success("System Online")
    st.info("Powered by Gemini LLM & RAG")

st.title(" Smart Library AI Agent")
st.caption("Context-Aware Digital Librarian for Engineering Students")

with st.expander(" Project Information & Usage Options"):
    st.write("This AI agent uses a Retrieval-Augmented Generation (RAG) pipeline to fetch real-time book availability, recommend syllabus-aligned resources, and provide academic guidance.")
    st.write("**Try asking things like:**")
    st.write("- *'Is Let us C available in the library?'*")
    st.write("- *'Suggest some books for 1st-semester programming.'*")

@st.cache_data
def load_data():
    paths = [
        "library_database.csv", 
        "Alternative_Live_UI_App/library_database.csv",
        "../library_database.csv"
    ]
    for path in paths:
        if os.path.exists(path):
            return pd.read_csv(path)
    return None

library_df = load_data()

api_key = st.secrets.get("GEMINI_API_KEY", "")
model = None

if api_key:
    genai.configure(api_key=api_key)
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                model = genai.GenerativeModel(m.name)
                break
    except Exception as e:
        st.error(f"System Error: {e}")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome! I'm your digital librarian. Which book or subject are you looking for today?"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter your query here..."):
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        
    with st.chat_message("assistant"):
        if not model:
            st.warning("API connection restricted. Please configure settings.")
        else:
            with st.spinner("Scanning library catalog..."):
                try:
                    context = library_df.head(20).to_string() if library_df is not None else "No database found."
                    
                    full_prompt = f"""You are a helpful Smart Library AI Agent for engineering students. 
                    Use the following library catalog data to answer the student's query accurately: \n\n{context}\n\n
                    Student's Query: {prompt}"""
                    
                    response = model.generate_content(full_prompt)
                    ai_reply = response.text
                    
                    st.markdown(ai_reply)
                    
                    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
                    
                except Exception as e:
                    st.error(f"Catalog Error: {e}")               
                    st.error(f"An error occurred: {e}")
