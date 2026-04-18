import streamlit as st
import google.generativeai as genai

# -------------------------------
# Secure API Setup
# -------------------------------
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel("gemini-pro")
except Exception as e:
    st.error("⚠️ API Key not found. Please add it in Streamlit Secrets.")
    st.stop()

# -------------------------------
# UI
# -------------------------------
st.title("🤖 AI Interview Assistant")
st.markdown("### 🚀 Practice interviews with AI-powered evaluation")

role = st.selectbox("Select Role", [
    "python developer",
    "web developer",
    "data scientist",
    "cloud engineer"
])

level = st.selectbox("Select Level", ["easy", "medium", "hard"])

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

    # Generate AI Questions
    try:
        with st.spinner("🤖 Generating questions..."):
            prompt = f"""
            Generate 3 {level} level interview questions for a {role}.
            Only return questions in numbered format.
            """

            response = model.generate_content(prompt)
            questions_ai = [q for q in response.text.split("\n") if q.strip() != ""]

    except Exception as e:
        st.error("❌ Error generating questions. Check API key or internet.")
        st.stop()

    st.subheader("🎤 Interview Questions")

    answers = []

    for i, q in enumerate(questions_ai):
        ans = st.text_input(q, key=f"q_{i}")
        answers.append(ans)

    # -------------------------------
    # Submit Answers
    # -------------------------------
    if st.button("Submit Answers"):

        if any(ans.strip() == "" for ans in answers):
            st.warning("⚠️ Please answer all questions before submitting.")
        else:
            try:
                with st.spinner("🧠 Evaluating your answers..."):

                    full_text = ""
                    for i in range(len(answers)):
                        full_text += f"Q: {questions_ai[i]}\nA: {answers[i]}\n\n"

                    eval_prompt = f"""
                    Evaluate the following interview answers.

                    {full_text}

                    Give:
                    1. Score out of 10
                    2. Strengths
                    3. Weaknesses
                    4. Suggestions
                    """

                    result = model.generate_content(eval_prompt)

                    st.subheader("🧠 AI Feedback")
                    st.write(result.text)

                    st.balloons()

            except Exception as e:
                st.error("❌ Error evaluating answers. Try again.")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.markdown("Made by Aryan 🚀")