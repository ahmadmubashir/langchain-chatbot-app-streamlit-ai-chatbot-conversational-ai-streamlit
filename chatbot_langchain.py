import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

st.title("🤖 Chatbot Developed by Mubashir")

# Initialize model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)

# Initialize conversation memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show conversation history
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        st.write(f"You: {msg.content}")
    else:
        st.write(f"AI: {msg.content}")

# Input area always at the bottom
user_input = st.text_input("You:", key="input_box")

send = st.button("Send")

if send and user_input:

    # Exit condition
    if user_input.lower() in ["exit", "quit", "bye"]:
        st.success("Conversation ended.")
        st.stop()

    # Add user message
    st.session_state.messages.append(HumanMessage(content=user_input))

    # Generate AI response
    response = llm.invoke(st.session_state.messages)

    # Add AI response
    st.session_state.messages.append(AIMessage(content=response.content))

    # Refresh UI so textbox appears again
    st.rerun()
