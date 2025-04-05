from flask import Flask, render_template, request, redirect, url_for, session
import json
import os

app = Flask(__name__)
app.secret_key = 'quiz_secret_key'

# Load questions from a default JSON file (questions.json)
with open("questions.json") as f:
    QUESTIONS = json.load(f)
with open("dsa.json") as f:
    DSA_QUESTIONS = json.load(f)

# Route to show the index page and initialize the session
@app.route('/')
def index():
    session['score'] = 0
    session['q_index'] = 0
    return render_template("index.html")

# Route for the default quiz
@app.route('/quiz', methods=["GET", "POST"])
def default_quiz():
    q_index = session.get('q_index', 0)
    category = "default"

    if request.method == 'POST':
        selected = request.form.get('option')
        correct = QUESTIONS[q_index - 1]['answer']
        if selected == correct:
            session['score'] += 1

    if q_index < len(QUESTIONS):
        question = QUESTIONS[q_index]
        session['q_index'] += 1
        return render_template("quiz.html", question=question, q_num=q_index + 1, category=category)
    else:
        return redirect(url_for('result'))

# Route to display the result of the default quiz
@app.route('/result')
def result():
    score = session.get('score', 0)
    total = len(QUESTIONS)
    return render_template("result.html", score=score, total=total)

# Route to show the available categories (quizzes)
@app.route('/categories')
def categories():
    available = [f.split('.')[0] for f in os.listdir("quizzes") if f.endswith(".json")]
    return render_template("categories.html", categories=available)

# Route for category-based quizzes
@app.route('/quiz/<category>', methods=["GET", "POST"])
def category_quiz(category):
    filepath = f"quizzes/{category}.json"
    
    # Check if the requested category exists
    if not os.path.exists(filepath):
        return "Invalid Category", 404

    # Load quiz data into the session if it's a new quiz or category
    if 'quiz_data' not in session or session.get('category') != category:
        with open(filepath) as f:
            session['quiz_data'] = json.load(f)
        session['quiz_index'] = 0
        session['quiz_score'] = 0
        session['category'] = category

    questions = session['quiz_data']
    index = session['quiz_index']

    # Handle POST requests for each question answered
    if request.method == 'POST':
        selected = request.form.get('option')
        correct = questions[index - 1]['answer']
        if selected == correct:
            session['quiz_score'] += 1

    # If there are more questions, render the next question
    if index < len(questions):
        session['quiz_index'] += 1
        return render_template('quiz_question.html',
                               question=questions[index],
                               q_num=index + 1,
                               total=len(questions),
                               category=category)
    else:
        # If all questions are answered, redirect to results
        score = session['quiz_score']
        total = len(questions)
        return redirect(url_for('quiz_result', score=score, total=total, category=category))

# Route to show results for a category-based quiz
@app.route('/quiz_result')
def quiz_result():
    score = request.args.get('score', 0, type=int)
    total = request.args.get('total', 0, type=int)
    category = request.args.get('category', 'default')
    return render_template("quiz_result.html", score=score, total=total, category=category)

# Main entry point to run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
