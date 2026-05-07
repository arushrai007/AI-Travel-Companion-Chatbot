import streamlit as st
import cohere
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title="🌍 AI Travel Companion", page_icon="🧳", layout="wide")

# ==========================================
# 🧠 MACHINE LEARNING PIPELINE (Price Predictor)
# ==========================================
@st.cache_resource
def train_prediction_model():
    """Trains a Random Forest model on mock historical flight data."""
    np.random.seed(42)
    # Generate 1000 rows of dummy flight data
    data = {
        'days_until_flight': np.random.randint(1, 90, 1000),
        'flight_duration_hours': np.random.uniform(1, 15, 1000),
        'airline_class': np.random.choice(['Economy', 'Business', 'First Class'], 1000),
    }
    df = pd.DataFrame(data)
    
    # Create realistic price logic (longer flights + better class = higher price)
    base_price = 150 + (df['flight_duration_hours'] * 45)
    class_multiplier = df['airline_class'].map({'Economy': 1, 'Business': 2.5, 'First Class': 4.5})
    booking_penalty = np.where(df['days_until_flight'] < 14, (14 - df['days_until_flight']) * 15, 0) # Expensive if booked late
    
    df['price'] = (base_price * class_multiplier) + booking_penalty
    
    # Encode text labels to numbers for the ML model
    le = LabelEncoder()
    df['airline_class_encoded'] = le.fit_transform(df['airline_class'])
    
    # Train the Random Forest Regressor
    X = df[['days_until_flight', 'flight_duration_hours', 'airline_class_encoded']]
    y = df['price']
    model = RandomForestRegressor(n_estimators=50, random_state=42)
    model.fit(X, y)
    
    return model, le

# Load the trained ML model
price_model, label_encoder = train_prediction_model()


# ==========================================
# 🖥️ STREAMLIT USER INTERFACE
# ==========================================

# Split the screen into a Sidebar (ML Predictor) and Main Area (AI Chatbot)
sidebar_col, main_col = st.columns([1, 2])

# --- SIDEBAR: ML PRICE PREDICTOR ---
with st.sidebar:
    st.header("📈 ML Price Predictor")
    st.markdown("Predict the cost of your flight using our Random Forest Regression model.")
    
    # User Inputs for the ML Model
    days_out = st.slider("Days until flight:", min_value=1, max_value=90, value=30)
    duration = st.slider("Flight duration (hours):", min_value=1.0, max_value=15.0, value=5.5, step=0.5)
    travel_class = st.selectbox("Class:", ["Economy", "Business", "First Class"])
    
    if st.button("🔮 Predict Price"):
        # Format the user input for the model
        class_encoded = label_encoder.transform([travel_class])[0]
        user_data = pd.DataFrame({
            'days_until_flight': [days_out],
            'flight_duration_hours': [duration],
            'airline_class_encoded': [class_encoded]
        })
        
        # Run the Prediction
        predicted_price = price_model.predict(user_data)[0]
        
        st.success(f"### Estimated Fare: ${predicted_price:,.2f}")
        st.caption("Based on historical data patterns.")

# --- MAIN AREA: AI TRAVEL CHATBOT ---
with main_col:
    st.title("🧳 AI Travel Companion Chatbot")
    st.markdown("Ask travel-related questions or ask the AI to build an itinerary based on your predicted flight price!")

    api_key = st.text_input("kR24ElUotvNUIUncuXoaAAFn3g1OqHaDPMt4j54m:", type="password")

    if api_key:
        co = cohere.Client(api_key)

        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Render existing messages
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["text"])

        user_input = st.chat_input("Ask me your travel-related question!")

        if user_input:
            # Append user message
            st.session_state.messages.append({"role": "user", "text": user_input})
            with st.chat_message("user"):
                st.markdown(user_input)

            preamble = """You are an AI Travel Companion. You ONLY answer travel-related questions. 
            If the user asks anything unrelated to travel, politely respond with: 'I am here to help only with travel-related questions 😊.'"""

            cohere_chat_history = []
            for msg in st.session_state.messages[:-1]:
                cohere_role = "USER" if msg["role"] == "user" else "CHATBOT"
                cohere_chat_history.append({"role": cohere_role, "message": msg["text"]})

            with st.spinner("Generating travel advice..."):
                try:
                    # Using the updated model from September 2024
                    response = co.chat(
                        model="command-r-plus-08-2024",
                        message=user_input,
                        preamble=preamble,
                        chat_history=cohere_chat_history,
                        temperature=0.7,
                        max_tokens=500
                    )
                    reply = response.text.strip()
                except Exception as e:
                    reply = f"❌ Error: {e}"

            st.session_state.messages.append({"role": "assistant", "text": reply})
            with st.chat_message("assistant"):
                st.markdown(reply)

st.markdown("""---  
**Created by Arush and Suresh** """, unsafe_allow_html=True)
