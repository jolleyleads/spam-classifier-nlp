from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.route("/", methods=["GET", "POST"])
def index():

    prediction = None
    message = ""

    if request.method == "POST":

        message = request.form["message"]

        # Convert text
        message_vectorized = vectorizer.transform([message])

        # Predict
        result = model.predict(message_vectorized)[0]

        if result == 1:
            prediction = "Spam"
        else:
            prediction = "Not Spam"

    return render_template(
        "index.html",
        prediction=prediction,
        message=message
    )

if __name__ == "__main__":
    app.run(debug=True)