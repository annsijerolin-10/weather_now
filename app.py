from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "f7cca314db04dd732819425c25181539"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            data = response.json()

            print("API Response:", data)  # Debugging line to check API response

            if response.status_code == 200:
                weather = {
                    "city": data["name"],
                    "temperature": data["main"]["temp"],
                    "description": data["weather"][0]["description"].capitalize(),
                    "humidity": data["main"]["humidity"],
                    "wind_speed": data["wind"]["speed"]
                }
            else:
                weather = {"error": "City not found. Please try again."}

    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)


