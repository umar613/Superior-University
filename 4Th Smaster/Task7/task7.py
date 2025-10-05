from flask import Flask, render_template, request
import requests

app = Flask(__name__)

NASA_API = "Ob2JBkQkBl4UKoML73KPHwgTR1XnmgZtefSZQfnX"
NASA_APOD_URL = "https://api.nasa.gov/planetary/apod"

@app.route('/', methods=['GET'])
def index():
    date = request.args.get('date')
    params = {
        "api_key": NASA_API,

    }
    if data:
        params ["date"] = date

    try:
        response = requests.get(NASA_APOD_URL, params=params)
        response.raise_for_status()
        data = response.json()
    except requests.requestsException as e:
        data = {
            "error": "failed to fetch data from NASA",
            "details": str(e)   
        }
    return render_template('index.html', apod_data=data)

if __name__ == '__main__':
    app.run(debug=True)



