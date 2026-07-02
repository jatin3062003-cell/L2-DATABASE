import streamlit as st
import requests

API_URL = "http://localhost:8000/chat"

def show():

    st.title("💬 L2 Database Assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Ask anything about your database..."):

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):

            placeholder = st.empty()

            try:
                with st.spinner("Thinking..."):

                    response = requests.post(
                        API_URL,
                        json={
                            "query": prompt
                        },
                        timeout=180
                    )

                    response.raise_for_status()

                    data = response.json()

                    if data.get("success"):
                        answer = data.get("answer", "")
                    else:
                        answer = "Something went wrong."

            except Exception as e:
                answer = f"❌ {e}"

            placeholder.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )