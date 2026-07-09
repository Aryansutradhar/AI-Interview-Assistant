import streamlit as st
from questions import get_questions
from evaluation import evaluate_answers
from report import generate_report, convert_to_csv


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="AI Interview Assistant",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------

st.markdown("""
<style>

.main{
    padding-top:20px;
}

.stButton>button{
    width:100%;
    height:50px;
    border-radius:10px;
    font-size:18px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Session State
# -----------------------------

if "started" not in st.session_state:
    st.session_state.started = False

if "questions" not in st.session_state:
    st.session_state.questions = []

# -----------------------------
# Title
# -----------------------------

st.title("🤖 AI Interview Assistant")

st.write(
    "Practice technical interviews with instant evaluation and performance feedback."
)

# -----------------------------
# Company
# -----------------------------

company = st.selectbox(

    "🏢 Select Company",

    [
        "TCS",
        "Infosys",
        "Wipro",
        "Accenture",
        "Cognizant"
    ]

)

# -----------------------------
# Role
# -----------------------------

role = st.selectbox(

    "💼 Select Role",

    [
        "python developer",
        "web developer",
        "data scientist",
        "cloud engineer"
    ]

)

# -----------------------------
# Level
# -----------------------------

level = st.selectbox(

    "📚 Difficulty",

    [
        "easy",
        "medium",
        "hard"
    ]

)

# -----------------------------
# Interview Round
# -----------------------------

round_type = st.selectbox(

    "🎯 Interview Round",

    [
        "Technical",
        "HR",
        "Aptitude"
    ]

)

# -----------------------------
# Start Interview
# -----------------------------

if st.button("🚀 Start Interview"):

    st.session_state.started = True

    st.session_state.questions = get_questions(
        role,
        level
    )

# -----------------------------
# Interview Questions
# -----------------------------

if st.session_state.started:

    st.divider()

    st.subheader("🎤 Interview Started")

    st.write("🏢 Company :", company)
    st.write("💼 Role :", role.title())
    st.write("🎯 Round :", round_type)
    st.write("📚 Level :", level.title())

    st.divider()

    answers = []

    total_questions = len(st.session_state.questions)

    for i, question in enumerate(st.session_state.questions):

        st.markdown(f"### Question {i+1} of {total_questions}")

        st.progress((i + 1) / total_questions)

        st.info(question)

        answer = st.text_area(

            "Your Answer",

            key=f"answer_{i}",

            height=150

        )

        answers.append(answer)

    st.divider()

    submit = st.button("✅ Submit Interview")

# -----------------------------
# Evaluation
# -----------------------------

    if submit:

        result = evaluate_answers(
            role,
            answers
        )

        st.divider()

        st.header("📊 Interview Results")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Score",
                f"{result['score']}/{result['max_score']}"
            )

        with col2:
            st.metric(
                "Accuracy",
                f"{result['accuracy']}%"
            )

        with col3:
            st.metric(
                "Performance",
                result["performance"]
            )

        st.progress(result["accuracy"] / 100)

        st.divider()

        st.subheader("💪 Strengths")

        if result["strengths"]:

            for item in result["strengths"]:

                st.success(item)

        else:

            st.info("No strengths detected.")

        st.subheader("⚠️ Areas to Improve")

        if result["weaknesses"]:

            for item in result["weaknesses"]:

                st.warning(item)

        else:

            st.success("Excellent! No major weaknesses.")

        st.divider()

        st.subheader("📝 Interview Summary")

        st.write(f"🏢 **Company:** {company}")
        st.write(f"💼 **Role:** {role.title()}")
        st.write(f"🎯 **Round:** {round_type}")
        st.write(f"📚 **Level:** {level.title()}")
        st.write(f"❓ **Questions Asked:** {len(st.session_state.questions)}")
        st.write(f"📊 **Score:** {result['score']}/{result['max_score']}")
        st.write(f"📈 **Accuracy:** {result['accuracy']}%")
        st.write(f"⭐ **Performance:** {result['performance']}")

        report = generate_report(
            company,
            role,
            level,
            round_type,
            st.session_state.questions,
            answers,
            result
        )

        csv = convert_to_csv(report)

        st.download_button(
            label="📥 Download Interview Report",
            data=csv,
            file_name="interview_report.csv",
            mime="text/csv"
        )

        st.balloons()

# -----------------------------
# Footer
# -----------------------------

st.divider()

st.markdown(
    "<center><h4>🤖 AI Interview Assistant</h4>"
    "<p>Developed by <b>Aryan Sutradhar</b> 🚀</p></center>",
    unsafe_allow_html=True
)