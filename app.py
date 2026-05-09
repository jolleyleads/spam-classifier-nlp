from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    message = ""

    if request.method == "POST":
        message = request.form["message"]
        message_vectorized = vectorizer.transform([message])
        result = model.predict(message_vectorized)[0]
        prediction = "Spam" if result == 1 else "Not Spam"

    return render_template("index.html", prediction=prediction, message=message)

@app.route("/predict", methods=["POST"])
def predict_api():
    data = request.get_json()
    message = data["message"]

    message_vectorized = vectorizer.transform([message])
    result = model.predict(message_vectorized)[0]
    prediction = "Spam" if result == 1 else "Not Spam"

    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(debug=True)