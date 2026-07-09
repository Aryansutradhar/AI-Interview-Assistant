import pandas as pd


def generate_report(
    company,
    role,
    level,
    round_type,
    questions,
    answers,
    result
):
    """
    Generate interview report as a DataFrame.
    """

    report = pd.DataFrame({

        "Question": questions,

        "Answer": answers

    })

    report["Company"] = company
    report["Role"] = role
    report["Level"] = level
    report["Round"] = round_type

    report["Score"] = f"{result['score']}/{result['max_score']}"
    report["Accuracy"] = f"{result['accuracy']}%"
    report["Performance"] = result["performance"]

    return report


def convert_to_csv(report):
    """
    Convert DataFrame to CSV.
    """

    return report.to_csv(index=False).encode("utf-8")