from flask import Flask, render_template, request
from utils import check_strength, is_common_password, suggest_stronger_password

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    score = None
    feedback = []
    suggestion = None

    if request.method == "POST":
        password = request.form["password"]
        score, feedback = check_strength(password)

        if is_common_password(password):
            feedback.append("⚠️ This is a very common password. Avoid using it.")
            score = max(score - 1, 0)

        if score < 4:
            suggestion = suggest_stronger_password(password)

    return render_template("index.html", password=password, score=score, feedback=feedback, suggestion=suggestion)

if __name__ == "__main__":
    if __name__ == "__main__":
     app.run(host='0.0.0.0', port=10000)


