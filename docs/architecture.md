\# Architecture Diagram



```mermaid

flowchart TD

&#x20;   A\[User enters message] --> B\[Flask Web App]

&#x20;   B --> C\[Text Preprocessing]

&#x20;   C --> D\[NLP Vectorizer]

&#x20;   D --> E\[Trained Spam Classifier]

&#x20;   E --> F\[Prediction: Spam or Not Spam]

&#x20;   F --> G\[Result shown in browser]

```

