import streamlit as st
import pandas as pd
from openai import OpenAI

#  Page Configuration
st.set_page_config(page_title="Smart Library AI Agent", page_icon="📚", layout="centered")

st.title("📚 Smart Library AI Agent")
st.markdown("Hello! I am your AI-powered digital librarian. Ask me about books, syllabus resources, or real-time availability.")

#  Load the Library Database
@st.cache_data
def load_data():
    try:
        # Load your CSV file
        df = pd.read_csv("library_database.csv")
        return df
    except FileNotFoundError:
        return None

library_df = load_data()

# Setup OpenAI Client
# In Streamlit Cloud, you will securely save the API key in the 'Secrets' section
api_key = st.secrets.get("OPENAI_API_KEY", "")
client = OpenAI(api_key=api_key)

# Initialize Chat History
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
        
    # Generate AI Response
    with st.chat_message("assistant"):
        if not api_key:
            st.warning("Please configure your OpenAI API Key to generate responses.")
        else:
            with st.spinner("Searching catalog and thinking..."):
                try:
                    context = library_df.head(10).to_string() if library_df is not None else "No database found."
                    
                    system_prompt = f"""You are a helpful Smart Library AI Agent for engineering students. 
                    Use the following library catalog data to answer the student's query: \n\n{context}"""
                    
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo", 
                        messages=[
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": prompt}
                        ]
                    )
                    
                    ai_reply = response.choices[0].message.content
                    st.markdown(ai_reply)
                    
                    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
                    
                except Exception as e:
                    st.error(f"An error occurred: {e}")
