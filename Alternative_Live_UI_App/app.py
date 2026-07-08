import streamlit as st
import pandas as pd
import google.generativeai as genai

#  Page Configuration
st.set_page_config(page_title="Smart Library AI Agent", page_icon="📚", layout="centered")

st.title("📚 Smart Library AI Agent")
st.markdown("Hello! I am your AI-powered digital librarian. Ask me about books, syllabus resources, or real-time availability.")

#  Load the Library Database
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("library_database.csv")
        return df
    except FileNotFoundError:
        return None

library_df = load_data()

api_key = st.secrets.get("GEMINI_API_KEY", "")
if api_key:
    genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')



if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "How can I help you find study materials today?"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("E.g., Is 'Let us C' available?"):
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        
    with st.chat_message("assistant"):
        if not model:
            st.warning("Please configure your GEMINI API Key in Streamlit settings.")
        else:
            with st.spinner("Searching catalog and thinking..."):
                try:
                    context = library_df.head(10).to_string() if library_df is not None else "No database found."
                    
                    full_prompt = f"""You are a helpful Smart Library AI Agent for engineering students. 
                    Use the following library catalog data to answer the student's query: \n\n{context}\n\n
                    Student's Query: {prompt}"""
                    
                    response = model.generate_content(full_prompt)
                    ai_reply = response.text
                    
                    st.markdown(ai_reply)
                    
                    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
                    
                except Exception as e:
                    st.error(f"An error occurred: {e}")
