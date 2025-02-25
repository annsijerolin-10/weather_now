from flask import Flask, request, render_template
import requests
import os
import logging

app = Flask(__name__)
API_KEY = os.getenv("WEATHER_API_KEY")  # Store API key securely

logging.basicConfig(level=logging.DEBUG)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        city = request.form["city"]
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)
        data = response.json()
        app.logger.debug(f"API Response: {data}")  # Debugging

        if response.status_code == 200 and "main" in data:
            return render_template("index.html", weather=data)
        else:
            error_message = data.get("message", "City not found")
            return render_template("index.html", error=error_message)

    return render_template("index.html", weather=None)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
