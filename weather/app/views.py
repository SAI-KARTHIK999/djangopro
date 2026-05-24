from django.shortcuts import render
import requests

API_KEY = "f6720fb1bc4091f89ed15e21f6a90bd6"

def weather_view(request):
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.POST.get("city")

        url = (
            "https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={API_KEY}&units=metric"
        )

        response = requests.get(url)
        data = response.json()

        if str(data.get("cod")) != "200":
            error = data.get("message", "City not found.")
        else:
            weather_data = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"].title(),
            }

    return render(request, "weather.html", {
        "weather": weather_data,
        "error": error,
    })