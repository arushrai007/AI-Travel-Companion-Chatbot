import streamlit as st
import cohere

st.set_page_config(page_title="🌍 AI Travel Companion", page_icon="🧳")
st.title("🧳 AI Travel Companion Chatbot")
st.markdown("Ask travel-related questions only: destinations, budget trips, safety, packing tips, etc.")

api_key = st.text_input("UZCA72sepSuswT5iXjA3oekkTu1jlmKAOr0I6PH6", type="password")

if api_key:
    co = cohere.Client(api_key)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    user_input = st.chat_input("Ask me your travel-related question!")

    if user_input:
        st.session_state.messages.append({"role": "user", "text": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        prompt = """You are an AI Travel Companion. You ONLY answer travel-related questions such as destinations, travel tips, budgeting, itineraries, packing, transportation, accommodations, and safety.

If the user asks anything unrelated to travel, politely respond with: "I'm here to help only with travel-related questions 😊. Please ask something related to your trip!"

Previous conversation:
"""

        for msg in st.session_state.messages:
            role = "User" if msg["role"] == "user" else "Assistant"
            prompt += f"{role}: {msg['text']}\n"
        prompt += "Assistant:"

        with st.spinner("Generating travel advice..."):
            try:
                response = co.generate(
                    model="command-r-plus",
                    prompt=prompt,
                    max_tokens=500,
                    temperature=0.7,
                    stop_sequences=["User:"],
                    truncate="END"
                )
                reply = response.generations[0].text.strip()
            except Exception as e:
                reply = f"❌ Error: {e}"

        st.session_state.messages.append({"role": "assistant", "text": reply})
        with st.chat_message("assistant"):
            st.markdown(reply)

    for msg in st.session_state.messages:
        with st.chat_message("user" if msg["role"] == "user" else "assistant"):
            st.markdown(msg["text"])

st.markdown("""---  
**Created by Arush and Suresh**  
""", unsafe_allow_html=True)
