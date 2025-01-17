from flask import Flask, request, render_template_string, abort
import os

app = Flask(__name__)

FLAG = os.getenv("FLAG", "ctf{dummy_flag}")

@app.route("/")
def index():
    return open("templates/index.html").read()

@app.route("/greet", methods=["POST"])
def greet():
    username = request.form.get("username", "Guest")
    template = f"""
    <div class="container text-center">
        <h1>Hello, {username}!</h1>
        <p>Try to find the hidden message!</p>
        <a href="/" class="btn btn-secondary mt-3">Go Back</a>
    </div>
    """
    try:
        return render_template_string(template)
    except Exception as e:
        abort(400, "Invalid input")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
