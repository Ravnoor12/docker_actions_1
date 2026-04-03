from flask import Flask, render_template, request

app = Flask(__name__)

# Route 1: The actual web page
@app.route("/")
def home():
    # render_template looks in the "templates" folder for index.html
    return render_template("index.html", title="My Awesome Site")

# Route 2: Where the form sends its data
@app.route("/submit", methods=["POST"])
def submit():
    # Grab the 'username' the user typed into the form
    user = request.form.get("username")
    return f"Thank you for logging in, {user}!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)