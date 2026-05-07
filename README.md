## 🌍 AI Travel Companion Chatbot

An **AI-powered travel assistant** built using **Python**, **Streamlit**, and **Cohere's Command R+ API**. This chatbot helps users plan trips, discover destinations, and get travel tips through an interactive chat interface.

---

## 🧭 Overview

The **AI Travel Companion Chatbot** provides personalized and context-aware travel assistance. Users can ask about destinations, get itinerary suggestions, or request travel safety information — all within an intuitive web interface.

---

## 🧰 Languages & Tools

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Cohere_API-000000?style=for-the-badge&logo=cohere&logoColor=white"/>
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white"/>
  <img src="https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white"/>
</p>

---

## 🚀 Features

* 💬 **Interactive Chat Interface** — Ask travel-related questions and receive detailed responses.
* 🌐 **Context-Aware Conversations** — Maintains chat history using Streamlit session state.
* 🗺️ **Dynamic Itinerary Suggestions** — Generates travel plans tailored to user preferences.
* 🧠 **Powered by AI** — Uses Cohere’s **Command R+** large language model for natural, human-like responses.

---

## 🛠️ Tools & Technologies

* **Python** — Core development language
* **Streamlit** — Web interface and session state management
* **Cohere API (Command R+)** — Natural language understanding and response generation

---

## ⚙️ Implementation Overview

The chatbot is implemented in **Streamlit**, enabling real-time chat interactions.
Cohere’s **Command R+ API** processes user prompts and generates relevant, context-aware travel responses.
Session state in Streamlit ensures that the conversation flow and context are preserved throughout the chat.

---

## 🧩 Project Structure

```
AI-Travel-Companion-Chatbot/
│
├── app.py                 # Main Streamlit application file
├── requirements.txt       # List of dependencies
├── README.md              # Project documentation
└── assets/                # (Optional) Images or additional resources
```

---

## ⚡ Installation & Usage

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/AI-Travel-Companion-Chatbot.git
cd AI-Travel-Companion-Chatbot
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set up Cohere API Key

Create a `.env` file in the project root and add your Cohere API key:

```
COHERE_API_KEY=your_api_key_here
```

### 4️⃣ Run the Streamlit app

```bash
streamlit run app.py
```

### 5️⃣ Start chatting!

Open the local URL shown in the terminal and begin your travel planning journey. 🌴✈️

---

## 🧠 Future Improvements

* 🌍 Integration with live flight & hotel APIs
* 🗣️ Voice-enabled chatbot functionality
* 🧳 Personalized user profiles and travel history tracking

---

## 🏁 Conclusion

The **AI Travel Companion Chatbot** demonstrates how **AI can enhance travel planning** by providing intelligent, conversational assistance. With seamless integration of **Cohere’s Command R+** and **Streamlit**, it offers an engaging and practical travel experience for users worldwide.

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use and modify it.

