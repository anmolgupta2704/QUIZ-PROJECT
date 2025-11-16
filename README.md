# 🧠 Quiz App — Flask Based

A modern, beautiful, and fully customizable Quiz Application where users can create quizzes, play multiple categories, and get instant results.
Styled with Glassmorphism + Gradients for a premium feel.

# Live Features
   ✨ Beautiful UI with gradients & glassmorphism

   📚 Multiple quiz categories

   📝 User-created quizzes with auto JSON saving

   📊 Score + percentage calculation

   🔄 Dynamic question flow

   📱 Fully responsive design

   ⚡ Fast & lightweight Flask app

    🎨 Professional UI on every page

   💾 Session-based tracking

# 🎯 Tech Stack

| Technology         | Used For               |
| ------------------ | ---------------------- |
| **Python / Flask** | Backend Logic, Routing |
| **HTML + CSS**     | UI Pages               |
| **Jinja2**         | Rendering Dynamic Data |
| **JSON**           | Storing Quiz Data      |
| **Sessions**       | Score Tracking         |

# 📁 Project Structure

```bash
quiz-app/
│
├── app.py
├── quizzes/
│   ├── html.json
│   ├── python.json
│   ├── dsa.json
│   └── (user quizzes saved here)
│
├── templates/
│   ├── index.html
│   ├── categories.html
│   ├── create_quiz.html
│   ├── quiz_question.html
│   ├── quiz_result.html
│   └── result.html
│
├── static/
│   └── style.css
│
├── .gitignore
└── README.md
```
# ⚙️ Installation

1️⃣ Clone Repo
```bash
git clone https://github.com/your-username/quiz-app.git
cd quiz-app
```
2️⃣ Create Virtual Environment
```bash
python -m venv venv
```
3️⃣ Activate Environment

```bash
venv\Scripts\activate
```
4️⃣ Install Requirements
```bash
pip install flask
```

5️⃣ Start App
```bash
python app.py
```