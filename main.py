from src.prediction import predict_aqi

# sample input
sample = [120, 180, 40, 10, 1.2, 30]

result = predict_aqi(sample)

print("Predicted AQI:", result)