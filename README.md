# Spam Classifier NLP

## Overview

Spam Classifier NLP is a machine learning web application that classifies text messages as spam or not spam using natural language processing and machine learning.

This project demonstrates an end-to-end NLP workflow including text preprocessing, TF-IDF vectorization, classification modeling, Flask integration, and deployment.

---

## Live Demo

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