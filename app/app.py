from flask import Flask, request, render_template
import sys
import os

# Add utils path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.grammar_utils import check_grammar

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    errors = []
    input_text = ""

    if request.method == "POST":
        input_text = request.form.get("text")
        if input_text.strip():
            results = check_grammar(input_text)
            if results:
                errors = results
            else:
                result = "No grammatical errors found."

    return render_template("index.html", input_text=input_text, result=result, errors=errors)

if __name__ == "__main__":
    app.run(debug=True)
