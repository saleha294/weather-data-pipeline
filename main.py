#Input → Process → Output: Every good function should answer three questions. Input? Raw weather dictionary. Process? Clean it, rename fields,
#  remove unnecessary data. Output? Clean dictionary. That's why your function 
# feels so natural.

from extract import extract_weather_data
from transform import transform_weather_data
from load import load_weather_data

raw_weather_data = extract_weather_data()
print(raw_weather_data)

cleaned_weather_data = transform_weather_data(raw_weather_data)
print(cleaned_weather_data)

load_weather_data(cleaned_weather_data)
