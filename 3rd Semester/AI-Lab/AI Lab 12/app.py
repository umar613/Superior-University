from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if not file:
            return "No file uploaded"
        df = pd.read_csv(file)

        # Fill missing values
        mode_cols = ['Likes', 'Dislikes', 'Category']
        for col in mode_cols:
            df[col] = df[col].fillna(df[col].mode()[0])

        # Drop rows with missing Category
        df.dropna(subset=['Category'], inplace=True)

        # Convert Likes and Dislikes to int
        for col in ['Likes', 'Dislikes']:
            df[col] = df[col].astype(str).str.replace(',', '').astype('int64')

        # Encode categorical columns
        df_clean = df.copy()
        le_cat = LabelEncoder()
        le_pub = LabelEncoder()
        df_clean['Category'] = le_cat.fit_transform(df_clean['Category'])
        df_clean['published'] = le_pub.fit_transform(df_clean['published'])

        # Create target column
        df_clean['top10'] = (df_clean['rank'] <= 10).astype(int)

        X = df_clean.drop(columns=['rank', 'Video', 'top10'])
        y = df_clean['top10']

        trainX, testX, trainY, testY = train_test_split(X, y, test_size=0.2, random_state=42)

        # Scale features
        scaler = StandardScaler()
        trainX_scaled = scaler.fit_transform(trainX)
        testX_scaled = scaler.transform(testX)

        # Train model
        clf = RandomForestClassifier(n_estimators=200, random_state=42)
        clf.fit(trainX_scaled, trainY)
        predictions = clf.predict(testX_scaled)
        accuracy = accuracy_score(testY, predictions)

        return f"<h2>Model Accuracy: {round(accuracy * 100, 2)}%</h2>"

    return render_template("index.html")
