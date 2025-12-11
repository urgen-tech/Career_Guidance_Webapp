import streamlit as st
import requests

st.set_page_config(page_title="Career Chatbot Assistant", page_icon="🤖")
st.title("🤖 Career Chatbot Assistant (Ollama)")

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "phi3"  # Change to the model you've pulled in Ollama

# Initialize message history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful career guidance assistant."}
    ]

# Display previous messages
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask me anything about your career...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Prepare request payload
    payload = {
        "model": MODEL_NAME,
        "messages": st.session_state.messages,
        "stream": False
    }

    # Send request to Ollama
    try:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = requests.post(OLLAMA_URL, json=payload, timeout=60)
                response.raise_for_status()
                result = response.json()
                reply = result["message"]["content"]
                st.markdown(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})

    except requests.exceptions.RequestException as e:
        st.error(f"Failed to connect to Ollama server: {str(e)}")
    except Exception as e:
        st.error(f"Something went wrong: {str(e)}")