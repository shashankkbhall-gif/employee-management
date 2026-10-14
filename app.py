
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

employees = []

@app.route("/")
def home():
    return render_template("index.html", employees=employees)

@app.route("/add", methods=["POST"])
def add_employee():
    name = request.form.get("name", "").strip()
    role = request.form.get("role", "").strip()

    if name and role:
        employees.append({
            "id": len(employees) + 1,
            "name": name,
            "role": role
        })

    return redirect(url_for("home"))

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
