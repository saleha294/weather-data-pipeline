# clean the weather data i.e set missing values for the qualities we need, then round off etc

def transform_weather_data(unclean_weather_data):

    current_weather = unclean_weather_data.get("current") #first get into current dictionary

    cleaned_weather_data = {
        "temperature" : current_weather.get("temperature_2m"),
        "humidity" : current_weather.get("relative_humidity_2m"),
        "wind_speed" : current_weather.get("wind_speed_10m"),
       "time" : current_weather.get("time"),
       "city" : "lahore"

    }

    return cleaned_weather_data