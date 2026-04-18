[![Live App](https://img.shields.io/badge/Streamlit-Live_App-red)](https://ai-interview-assistant-kvaozgetcd3xjwtnorws7b.streamlit.app/)

# 🤖 AI Interview Assistant

A smart interview preparation tool with AI integration and a built-in fallback system for real-world reliability.

---

## 🌐 Live Demo

[🚀 Click here to try the app](https://ai-interview-assistant-kvaozgetcd3xjwtnorws7b.streamlit.app/)

---

## 🚀 Features

* 🤖 AI-powered interview question generation (Gemini API)
* 🔁 Smart fallback system when AI is unavailable
* 🎯 Role-based interview (Python, Web Development, Data Science, Cloud)
* 📊 Answer evaluation with scoring and feedback
* 📈 Progress tracking with performance insights
* 🧠 Beginner-friendly and interactive UI

---

## ⚠️ Reliability Feature (Key Highlight)

This application uses a **hybrid architecture**.

If the AI API is unavailable due to:

* quota limits
* network issues
* API restrictions

👉 The system automatically switches to a **fallback question engine**

This ensures:

* ✅ No app crashes
* ✅ Continuous user experience
* ✅ Reliable performance

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Google Gemini API *(optional AI integration)*

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/aryansutradhar/ai-interview-assistant.git
cd ai-interview-assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

---

## 🔐 API Setup (Optional)

To enable AI features:

1. Get API key from Google AI Studio
2. Create a file:

```
.streamlit/secrets.toml
```

3. Add your API key:

```toml
GEMINI_API_KEY = "your_api_key_here"
```

👉 If not added, the app will automatically run in fallback mode.

---

## 🎯 How It Works

1. Select your role and difficulty level
2. Start the interview
3. Answer the questions
4. Receive instant feedback and score

---

## 💡 Project Highlights

* Hybrid AI + rule-based system
* Designed for real-world reliability
* Handles API failures gracefully
* Clean and interactive user interface

---

## 📸 Demo

*(Add screenshots here later to make your GitHub even more impressive)*

---

## 👨‍💻 Author

**Aryansutradhar** 🚀
Aspiring Software Developer

---

## ⭐ Future Improvements

* Resume-based question generation
* Advanced AI evaluation system
* Voice-based interview interaction
* Detailed analytics dashboard

---

