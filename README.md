# 🌍 Air Quality Predictor

## 📌 Project Overview

This project is a Machine Learning-based web application that predicts Air Quality Index (AQI) using pollution parameters like PM2.5, PM10, NO2, SO2, CO, and O3.

## 🚀 Features

* Predict AQI using trained ML model
* City-based AQI prediction
* Displays AQI category (Good, Moderate, Unhealthy, etc.)
* Simple and user-friendly web interface

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn (Random Forest)
* Flask (Web Framework)
* HTML, CSS

## 📂 Project Structure

* data/ → raw and processed data
* src/ → preprocessing, training, prediction logic
* models/ → saved ML model
* app/ → Flask web app

## ▶️ How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Run preprocessing:
   python src/data_preprocessing.py

3. Train model:
   python src/model_training.py

4. Run app:
   python -m app.app

5. Open in browser:
   http://127.0.0.1:5000/

## 📊 Sample Output

* User selects a city
* AQI is predicted
* Category is displayed

## 📌 Future Improvements

* Add live AQI API data
* Improve UI design
* Deploy online

## 🙌 Author

Shivendra Patel
