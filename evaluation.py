from keywords import get_keywords


def evaluate_answers(role, answers):

    score = 0

    strengths = []

    weaknesses = []

    for ans in answers:

        ans = ans.lower()

        words = ans.split()

        # Answer Length Score
        if len(words) >= 10:
            score += 1

        # Keyword Score
        matched = set()

        for word in get_keywords(role):

            if word in ans:
                matched.add(word)

        score += len(matched)

    # Maximum Possible Score
    max_score = len(answers) * (len(get_keywords(role)) + 1)

    # Accuracy
    accuracy = round((score / max_score) * 100, 2)

    # Performance
    if accuracy >= 80:
        performance = "Excellent"
        strengths = [
            "Strong technical concepts",
            "Detailed explanations",
            "Good use of technical keywords"
        ]

    elif accuracy >= 60:
        performance = "Good"
        strengths = [
            "Good understanding of concepts"
        ]

        weaknesses = [
            "Need more technical keywords",
            "Explain answers in more detail"
        ]

    else:
        performance = "Needs Improvement"

        weaknesses = [
            "Practice technical concepts",
            "Give longer answers",
            "Use more technical keywords"
        ]

    return {
        "score": score,
        "max_score": max_score,
        "accuracy": accuracy,
        "performance": performance,
        "strengths": strengths,
        "weaknesses": weaknesses
    }