# Spam Classifier NLP

## Overview

Spam Classifier NLP is a machine learning web application that classifies text messages as spam or not spam using natural language processing and machine learning.

This project demonstrates an end-to-end NLP workflow including text preprocessing, TF-IDF vectorization, classification modeling, Flask integration, and deployment.

---

## Live Demo
## Make.com Gmail Workflow Integration

This NLP classifier was integrated into a Make.com workflow to classify Gmail email content through the deployed Flask API.

### Live Workflow Architecture

```text
Gmail Email Input
→ Make.com HTTP Request
→ Deployed Flask NLP API on Render
→ JSON Prediction Response
→ Router Filter
→ Spam or Ham Route
```

### API Endpoint

```text
POST /predict
```

### Example Request

```json
{
  "message": "WIN free money now click here"
}
```

### Example Response

```json
{
  "prediction": "spam"
}
```

### What This Integration Demonstrates

* Deployed machine learning model exposed as a live API
* Flask backend with a prediction endpoint
* NLP text classification using TF-IDF and logistic regression
* Make.com workflow automation
* Gmail email input integration
* HTTP API request/response handling
* Router-based spam/ham business logic
* Real-world AI automation pipeline

**This shows the model is not only a standalone web app, but also a usable backend API that can power automated business workflows.**

https://spam-classifier-nlp.onrender.com/

---

## What This Project Shows

- Natural Language Processing (NLP)
- Text Classification
- TF-IDF Vectorization
- Logistic Regression Modeling
- Flask Web App Development
- Machine Learning Inference
- Deployment-Ready AI Applications

---

## Tech Stack

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- TF-IDF Vectorizer
- Logistic Regression
- HTML/CSS
- Render
- GitHub

---

## Business Use Case

This application demonstrates how machine learning can automatically identify spam messages for:

- customer communication filtering
- email/message moderation
- automated support systems
- message quality control
- AI-powered filtering systems

---

## How It Works

1. User enters a text message.
2. The application preprocesses the text.
3. TF-IDF vectorization converts the message into numerical features.
4. The trained classification model predicts whether the message is spam or not spam.
5. The prediction result is displayed in the browser.

---

## Machine Learning Workflow

1. Loaded labeled spam/ham dataset
2. Cleaned and prepared text data
3. Converted text into numerical vectors using TF-IDF
4. Trained a machine learning classification model
5. Saved the trained model and vectorizer
6. Connected the model to a Flask web application
7. Deployed the application online

---

## Project Structure

```text
spam-classifier-nlp/
├── app.py
├── train_model.py
├── model.pkl
├── vectorizer.pkl
├── spam.csv
├── requirements.txt
├── templates/
└── README.md
