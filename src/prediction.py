import joblib
import pandas as pd

model = joblib.load("models/aqi_model.pkl")

# cleaned data load
df = pd.read_csv("data/processed/aqi_cleaned.csv")

def predict_aqi(data):
    result = model.predict([data])
    return result[0]

def predict_by_city(city):
    # filter city data
    city_data = df[df['City'] == city]

    # average values
    avg = city_data[['PM2.5','PM10','NO2','SO2','CO','O3']].mean()

    # prediction
    result = model.predict([avg.values])

    return result[0]

def get_aqi_category(aqi):
    if aqi <= 50:
        return "Good 😊"
    elif aqi <= 100:
        return "Moderate 😐"
    elif aqi <= 200:
        return "Unhealthy 😷"
    else:
        return "Hazardous ☠️"

