from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("Login.html")  # Renderiza el template al inicio

@app.route("/Index")
def home():
    return render_template("Index.html")  # Renderiza el template al inicio


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
