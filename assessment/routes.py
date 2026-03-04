from flask import Blueprint, render_template, request, session, redirect
import sqlite3

# Blueprint creation
assessment_bp = Blueprint('assessment', __name__,
template_folder='../templates'
)

# ---------------- HOME ----------------
@assessment_bp.route("/")
def home():
    return render_template("assessment/home.html")


# ---------------- LEVEL PAGE ----------------
@assessment_bp.route("/levels/<topic>")
def levels(topic):
    return render_template("assessment/levels.html", topic=topic)


# ---------------- QUIZ PAGE ----------------
@assessment_bp.route("/quiz/<topic>/<level>")
def quiz(topic, level):

    conn = sqlite3.connect("assessment/cryptora.db")
    cur = conn.cursor()

    cur.execute("""
        SELECT *
        FROM questions
        WHERE topic=? AND level=?
        ORDER BY RANDOM()
        LIMIT 20
    """, (topic, level))

    questions = cur.fetchall()
    conn.close()

    return render_template(
        "assessment/quiz.html",
        topic=topic,
        level=level,
        questions=questions
    )


# ---------------- SUBMIT QUIZ ----------------
@assessment_bp.route("/submit/<topic>/<level>", methods=["POST"])
def submit(topic, level):

    conn = sqlite3.connect("assessment/cryptora.db")
    cur = conn.cursor()

    cur.execute("""
        SELECT id, answer
        FROM questions
        WHERE topic=? AND level=?
    """, (topic, level))

    correct_answers = cur.fetchall()

    score = 0
    total = 0

    for question_id, correct_answer in correct_answers:
        user_answer = request.form.get(f"q{question_id}")

        if user_answer:
            total += 1
            if user_answer == correct_answer:
                score += 1

    percentage = (score / total) * 100 if total > 0 else 0
    result = "PASS" if percentage >= 70 else "FAIL"

    if percentage < 40:
        status = "Weaker"
    elif percentage < 60:
        status = "Weak"
    elif percentage < 80:
        status = "Strong"
    else:
        status = "Stronger"

    cur.execute("""
        INSERT INTO results(topic, score, total, percentage, status)
        VALUES (?, ?, ?, ?, ?)
    """, (topic, score, total, percentage, status))

    conn.commit()
    conn.close()

    return render_template(
        "assessment/result.html",
        topic=topic,
        level=level,
        score=score,
        total=total,
        percentage=round(percentage, 2),
        result=result,
        status=status
    )


# ---------------- PROGRESS PAGE ----------------
@assessment_bp.route("/progress")
def progress():

    conn = sqlite3.connect("assessment/cryptora.db")
    cur = conn.cursor()

    cur.execute("SELECT topic, score, total, percentage, status FROM results")
    rows = cur.fetchall()

    conn.close()

    return render_template("assessment/progress.html", results=rows)


# ---------------- DASHBOARD ----------------
@assessment_bp.route("/dashboard")
def dashboard():

    conn = sqlite3.connect("assessment/cryptora.db")
    cur = conn.cursor()

    cur.execute("SELECT topic, score, total, percentage, status FROM results")
    results = cur.fetchall()

    conn.close()

    return render_template("assessment/dashboard.html", results=results)
