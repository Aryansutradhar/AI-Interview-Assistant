import random

questions = {

    "python developer": {

        "easy": [
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

        "medium": [
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

        "hard": [
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

    "web developer": {

        "easy": [
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

        "medium": [
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

        "hard": [
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

    "data scientist": {

        "easy": [
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

        "medium": [
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

        "hard": [
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

    "cloud engineer": {

        "easy": [
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

        "medium": [
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

        "hard": [
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


def get_questions(role, level):
    """
    Returns 5 random questions for the selected role and level.
    """
    return random.sample(questions[role][level], 5)