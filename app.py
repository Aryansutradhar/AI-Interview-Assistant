import streamlit as st
import random
import pandas as pd

# ---------------------------
# Page Config
# ---------------------------

st.set_page_config(
    page_title="AI Interview Assistant",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------
# Styling
# ---------------------------

st.markdown("""
<style>

.stButton>button{
width:100%;
height:50px;
border-radius:10px;
font-size:18px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# Session State
# ---------------------------

if "started" not in st.session_state:
    st.session_state.started=False

if "questions" not in st.session_state:
    st.session_state.questions=[]

# ---------------------------
# Questions
# ---------------------------

questions={

"python developer":{

"easy":[
"What is Python?",
"What is a list?",
"What is tuple?",
"What is dictionary?",
"What is variable?",
"What is function?",
"What is loop?",
"What is string?",
"What is module?",
"What is indentation?"
],

"medium":[
"Explain OOP concepts",
"What are decorators?",
"What is inheritance?",
"What is polymorphism?",
"What is encapsulation?",
"What are generators?",
"What are lambda functions?",
"What is exception handling?",
"What is file handling?",
"Difference between list and tuple"
],

"hard":[
"Explain GIL",
"Thread vs Process",
"What is multithreading?",
"What is multiprocessing?",
"What is metaclass?",
"What is async programming?",
"What is monkey patching?",
"What is context manager?",
"What is memory management?",
"What is Python internals?"
]

},

"web developer":{

"easy":[
"What is HTML?",
"What is CSS?",
"What is JavaScript?",
"What is browser?",
"What is hyperlink?",
"What is form?",
"What is Bootstrap?",
"What is responsive design?",
"What is div?",
"What is tag?"
],

"medium":[
"Difference between Flexbox and Grid",
"What is DOM?",
"What is AJAX?",
"What is JSON?",
"What is API?",
"What is local storage?",
"What is session storage?",
"GET vs POST",
"Explain event bubbling",
"What is responsive design?"
],

"hard":[
"What is REST API?",
"What is Event Delegation?",
"What is CORS?",
"What is JWT?",
"What is SSR?",
"What is CSR?",
"What is state management?",
"What is authentication?",
"What is WebSocket?",
"What is React lifecycle?"
]

},

"data scientist":{

"easy":[
"What is Data Science?",
"What is Pandas?",
"What is NumPy?",
"What is AI?",
"What is ML?",
"What is dataset?",
"What is CSV?",
"What is EDA?",
"What is data cleaning?",
"What is visualization?"
],

"medium":[
"What is overfitting?",
"What is underfitting?",
"What is classification?",
"What is regression?",
"What is supervised learning?",
"What is unsupervised learning?",
"What is normalization?",
"What is feature engineering?",
"What is training data?",
"What is model training?"
],

"hard":[
"What is ANN?",
"What is CNN?",
"What is RNN?",
"What is bias variance tradeoff?",
"What is cross validation?",
"What is gradient descent?",
"What is precision?",
"What is recall?",
"What is F1 score?",
"What is hyperparameter tuning?"
]

},

"cloud engineer":{

"easy":[
"What is Cloud?",
"What is AWS?",
"What is Azure?",
"What is GCP?",
"What is server?",
"What is storage?",
"What is virtualization?",
"What is SaaS?",
"What is PaaS?",
"What is IaaS?"
],

"medium":[
"What is Docker?",
"What is Kubernetes?",
"What is EC2?",
"What is subnet?",
"What is VPC?",
"What is DNS?",
"What is CI/CD?",
"What is load balancing?",
"What is auto scaling?",
"What is containerization?"
],

"hard":[
"Docker vs Kubernetes",
"What is Terraform?",
"What is orchestration?",
"What is microservices?",
"What is Infrastructure as Code?",
"What is distributed computing?",
"What is fault tolerance?",
"What is cloud security?",
"What is monitoring?",
"What is deployment?"
]

}

}

# ---------------------------
# Keywords
# ---------------------------

keywords={

"python developer":[
"python",
"class",
"function",
"object",
"thread",
"oop",
"inheritance"
],

"web developer":[
"html",
"css",
"javascript",
"api",
"frontend",
"backend",
"json"
],

"data scientist":[
"data",
"model",
"training",
"algorithm",
"pandas",
"numpy",
"cnn"
],

"cloud engineer":[
"cloud",
"aws",
"docker",
"kubernetes",
"server",
"deployment"
]

}

# ---------------------------
# Role Alias
# ---------------------------

role_alias={

"python":"python developer",
"py":"python developer",

"web":"web developer",

"data":"data scientist",
"ds":"data scientist",

"cloud":"cloud engineer",
"aws":"cloud engineer"

}

# ---------------------------
# UI
# ---------------------------

st.title("🤖 AI Interview Assistant")

st.markdown(
"Practice technical interviews with smart evaluation"
)

role=st.selectbox(
"Select Role",

[
"python developer",
"web developer",
"data scientist",
"cloud engineer"
]
)

level=st.selectbox(
"Select Level",
["easy","medium","hard"]
)

# ---------------------------
# Start
# ---------------------------

if st.button("Start Interview"):

    st.session_state.started=True

    st.session_state.questions=random.sample(
        questions[role][level],
        5
    )

# ---------------------------
# Questions
# ---------------------------

if st.session_state.started:

    st.subheader("🎤 Interview Questions")

    answers=[]

    for i,q in enumerate(
        st.session_state.questions
    ):

        st.progress(
            (i+1)/len(
                st.session_state.questions
            )
        )

        ans=st.text_area(
            q,
            key=f"q{i}"
        )

        answers.append(ans)

    # ---------------------------
    # Submit
    # ---------------------------

    if st.button(
        "Submit Answers"
    ):

        score=0

        for ans in answers:

            words=ans.lower().split()

            if len(words)>=10:
                score+=1

            matched=set()

            for word in keywords[role]:

                if word in ans.lower():

                    matched.add(word)

            score+=len(
                matched
            )

        max_score=(
        len(answers)*
        (
        len(
        keywords[role]
        )+1
        )
        )

        progress=score/max_score

        st.subheader(
        "📊 Performance"
        )

        st.write(
        f"Score : {score}/{max_score}"
        )

        st.write(
        f"Confidence : {round(progress*100,2)}%"
        )

        st.progress(progress)

        # Feedback

        if progress>.7:

            st.success(
            "🔥 Excellent Performance"
            )

        elif progress>.4:

            st.warning(
            "👍 Good but improve depth"
            )

        else:

            st.error(
            "❌ Practice more"
            )

        # Strengths

        st.subheader(
        "📌 Strengths"
        )

        if progress>.7:

            st.success(
            "✔ Strong technical concepts"
            )

            st.success(
            "✔ Detailed answers"
            )

        # Weakness

        st.subheader(
        "⚠ Weaknesses"
        )

        if progress<.7:

            st.warning(
            "Need deeper explanations"
            )

        if progress<.5:

            st.warning(
            "Use more technical terms"
            )

        # Report

        report=pd.DataFrame({

        "Question":
        st.session_state.questions,

        "Answer":
        answers

        })

        csv=report.to_csv(
        index=False
        )

        st.download_button(

        "📥 Download Report",

        csv,

        "interview_report.csv",

        "text/csv"

        )

        st.balloons()

st.markdown("---")
st.markdown(
"Made by Aryan 🚀"
)
