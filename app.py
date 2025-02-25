import streamlit as st
import google.generativeai as genai  

api_key = "AIzaSyA2nDXaXotiWi8g16GElwz20wOcRmO-j9U"  

# Title
st.title("Pk AI Chatbot")

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Previous Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input Handling
if prompt := st.chat_input("Enter your question..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        # Google Gemini AI Client
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-pro")

        # AI Response
        response = model.generate_content(prompt)
        assistant_message = response.text

        # Show Assistant Message
        st.chat_message("assistant").markdown(assistant_message)
        st.session_state.messages.append({"role": "assistant", "content": assistant_message})

    except Exception as e:
        st.error(f"Error: {e}")
