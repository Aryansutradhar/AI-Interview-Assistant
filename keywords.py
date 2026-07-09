keywords = {

    "python developer": [
        "python",
        "class",
        "object",
        "function",
        "loop",
        "list",
        "dictionary",
        "tuple",
        "inheritance",
        "polymorphism",
        "encapsulation",
        "decorator",
        "generator",
        "exception",
        "thread",
        "process",
        "async",
        "module",
        "package",
        "oop"
    ],

    "web developer": [
        "html",
        "css",
        "javascript",
        "dom",
        "api",
        "json",
        "ajax",
        "frontend",
        "backend",
        "responsive",
        "bootstrap",
        "react",
        "node",
        "express",
        "database",
        "authentication",
        "jwt",
        "cors",
        "rest",
        "websocket"
    ],

    "data scientist": [
        "python",
        "pandas",
        "numpy",
        "data",
        "model",
        "training",
        "algorithm",
        "classification",
        "regression",
        "cnn",
        "rnn",
        "ann",
        "machine learning",
        "feature",
        "dataset",
        "accuracy",
        "precision",
        "recall",
        "f1",
        "gradient"
    ],

    "cloud engineer": [
        "cloud",
        "aws",
        "azure",
        "gcp",
        "docker",
        "kubernetes",
        "server",
        "deployment",
        "terraform",
        "container",
        "vpc",
        "ec2",
        "dns",
        "load balancing",
        "autoscaling",
        "microservices",
        "security",
        "monitoring",
        "iac",
        "devops"
    ]

}


def get_keywords(role):
    """
    Returns keywords for the selected role.
    """
    return keywords[role]