from flask import Flask, render_template, request
from src.prediction import get_aqi_category, predict_by_city

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        city = request.form['city']
        result = predict_by_city(city)
        category = get_aqi_category(result)
        return render_template('index.html', prediction=result)
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)