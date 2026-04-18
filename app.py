import streamlit as st

# -------------------------------
# Try AI Setup
# -------------------------------
ai_available = True
try:
    from google import genai
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except:
    ai_available = False

# -------------------------------
# UI
# -------------------------------
st.title("🤖 AI Interview Assistant")
st.markdown("### 🚀 Practice interviews with AI-powered evaluation")

# Show mode
if ai_available:
    st.success("🤖 AI Mode Enabled")
else:
    st.warning("⚠️ Running in Basic Mode (No AI)")

# Instructions
st.markdown("""
### 📌 Instructions:
- Answer all questions clearly
- Try to give detailed answers
- AI mode may activate automatically
""")

# Role & Level
role = st.selectbox("Select Role", [
    "python developer",
    "web developer",
    "data scientist",
    "cloud engineer"
])

level = st.selectbox("Select Level", ["easy", "medium", "hard"])

# -------------------------------
# Fallback Questions (LEVEL BASED)
# -------------------------------
fallback_questions = {
    "python developer": {
        "easy": ["What is Python?", "What is a list?"],
        "medium": ["Explain OOP", "What are decorators?"],
        "hard": ["Explain GIL", "Thread vs Process"]
    },
    "web developer": {
        "easy": ["What is HTML?", "What is CSS?"],
        "medium": ["Flexbox vs Grid", "What is JavaScript?"],
        "hard": ["Event delegation", "REST API"]
    },
    "data scientist": {
        "easy": ["What is Data Science?", "What is Pandas?"],
        "medium": ["What is ML?", "What is Overfitting?"],
        "hard": ["Bias-variance tradeoff", "Cross-validation"]
    },
    "cloud engineer": {
        "easy": ["What is Cloud?", "What is AWS?"],
        "medium": ["IaaS vs PaaS vs SaaS", "Virtualization"],
        "hard": ["Load balancing", "Docker vs Kubernetes"]
    }
}

# -------------------------------
# Start Interview
# -------------------------------
if st.button("Start Interview"):
    st.session_state.started = True

# -------------------------------
# Interview Section
# -------------------------------
if "started" in st.session_state and st.session_state.started:

    st.info(f"🎯 Interview started for **{role}** ({level})")

    # Try AI Questions
    if ai_available:
        try:
            with st.spinner("🤖 Generating AI questions..."):

                prompt = f"Generate 3 {level} interview questions for a {role}"

                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=prompt
                )

                questions = [q for q in response.text.split("\n") if q.strip()]

        except:
            st.warning("⚠️ AI unavailable (quota issue), switching to smart fallback mode")
            questions = fallback_questions[role][level]

    else:
        questions = fallback_questions[role][level]

    # -------------------------------
    # Display Questions
    # -------------------------------
    st.subheader("🎤 Interview Questions")

    answers = []

    for i, q in enumerate(questions):
        ans = st.text_input(q, key=f"q_{i}")
        answers.append(ans)

    # -------------------------------
    # Submit Answers
    # -------------------------------
    if st.button("Submit Answers"):

        if any(a.strip() == "" for a in answers):
            st.warning("⚠️ Please answer all questions")
        else:
            st.subheader("📊 Performance")

            score = 0

            for ans in answers:
                if len(ans) > 20:
                    score += 1
                if any(word in ans.lower() for word in ["define", "example", "use"]):
                    score += 1

            max_score = len(answers) * 2
            progress = score / max_score

            st.write(f"Score: {score}/{max_score}")

            # Progress bar
            st.progress(progress)

            # Feedback
            if progress > 0.7:
                st.success("🔥 Excellent performance!")
            elif progress > 0.4:
                st.warning("👍 Good, but improve depth.")
            else:
                st.error("❌ Needs improvement. Practice more.")

            st.balloons()

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.markdown("Made by Aryan 🚀")