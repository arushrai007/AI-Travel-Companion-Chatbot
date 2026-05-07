import streamlit as st
import cohere

st.set_page_config(page_title="🌍 AI Travel Companion", page_icon="🧳")
st.title("🧳 AI Travel Companion Chatbot")
st.markdown("Ask travel-related questions only: destinations, budget trips, safety, packing tips, etc.")

# Prompt the user for the key instead of hardcoding it
api_key = st.text_input("kR24ElUotvNUIUncuXoaAAFn3g1OqHaDPMt4j54m:", type="password")

if api_key:
    co = cohere.Client(api_key)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # 1. Render existing messages first
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["text"])

    user_input = st.chat_input("Ask me your travel-related question!")

    if user_input:
        # Append user message to state and display it
        st.session_state.messages.append({"role": "user", "text": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # 2. Define instructions for the chatbot using 'preamble'
        preamble = """You are an AI Travel Companion. You ONLY answer travel-related questions such as destinations, travel tips, budgeting, itineraries, packing, transportation, accommodations, and safety.

If the user asks anything unrelated to travel, politely respond with: "I'm here to help only with travel-related questions 😊. Please ask something related to your trip!"
"""

        # 3. Format history for Cohere's Chat API
        cohere_chat_history = []
        for msg in st.session_state.messages[:-1]: # All messages EXCEPT the current one
            cohere_role = "USER" if msg["role"] == "user" else "CHATBOT"
            cohere_chat_history.append({"role": cohere_role, "message": msg["text"]})

        # 4. Use the new co.chat() API
        with st.spinner("Generating travel advice..."):
            try:
                response = co.chat(
                    model="command-r-plus",
                    message=user_input,
                    preamble=preamble,
                    chat_history=cohere_chat_history,
                    temperature=0.7,
                    max_tokens=500
                )
                reply = response.text.strip()
            except Exception as e:
                reply = f"❌ Error: {e}"

        # Append and render assistant response
        st.session_state.messages.append({"role": "assistant", "text": reply})
        with st.chat_message("assistant"):
            st.markdown(reply)

st.markdown("""---  
**Created by Arush** """, unsafe_allow_html=True)
