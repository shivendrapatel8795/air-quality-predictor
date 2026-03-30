from flask import Flask, render_template, request
from src.prediction import get_aqi_category, predict_by_city, predict_aqi

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':

        # check if ALL manual inputs filled
        pm25 = request.form.get('PM2.5')
        pm10 = request.form.get('PM10')
        no2 = request.form.get('NO2')
        so2 = request.form.get('SO2')
        co = request.form.get('CO')
        o3 = request.form.get('O3')

        if pm25 and pm10 and no2 and so2 and co and o3:
            # manual mode
            data = [
                float(pm25),
                float(pm10),
                float(no2),
                float(so2),
                float(co),
                float(o3)
            ]
            result = predict_aqi(data)
            mode = "Manual Input"

        else:
            # city mode
            city = request.form.get('city')
            result = predict_by_city(city)
            mode = "City Based"

        category = get_aqi_category(result)

        return render_template('index.html',
                               prediction=result,
                               category=category,
                               mode=mode)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)