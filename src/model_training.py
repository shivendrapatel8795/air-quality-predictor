import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# data load karo
df = pd.read_csv("data/processed/aqi_cleaned.csv")

# input (X) aur output (y)
X = df[['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3']]
y = df['AQI']

# data split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

# model banao
model = RandomForestRegressor()

# train karo
model.fit(X_train, y_train)

# model save karo
joblib.dump(model, "models/aqi_model.pkl")

print("Model trained and saved successfully!")