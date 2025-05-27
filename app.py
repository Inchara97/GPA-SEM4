from flask import Flask, render_template, request

app = Flask(__name__)

# Define fixed subjects and their credits
subjects = [
    ("Agile", 3),
    ("Calculus", 3),
    ("Machine Learning", 4),
    ("Computer Networks", 4),
    ("Blockchain", 3),
    ("GenAI", 3),
    ("UHV", 2),
    ("English", 2),
    ("Portfolio", 2),
    ("Elective", 2),
    ("Hons", 3)
]

@app.route("/", methods=["GET", "POST"])
def gpa_calculator():
    gpa = None
    if request.method == "POST":
        try:
            total_credits = 0
            total_points = 0

            for i, (subject, credit) in enumerate(subjects):
                grade_point = float(request.form[f"grade{i}"])
                total_credits += credit
                total_points += credit * grade_point

            gpa = round(total_points / total_credits, 2)
        except Exception:
            gpa = "Invalid input"

    return render_template("gpa_form.html", subjects=subjects, gpa=gpa)

if __name__ == "__main__":
    app.run(debug=True)
