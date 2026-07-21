#a file that has a function that fetches weather i.e 
# the Python code sends a GET request to the API using one of its endpoints (URL).
#The extract file should send the GET request and get the response.
#Extract shouldn't decide what's important.
#Extract's only responsibility is:
#"Go get the data."

import requests #requests library says, "Don't worry, I'll handle sending GET requests, receiving responses, errors, headers, and all that networking stuff."


def extract_weather_data():
    response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,relative_humidity_2m,wind_speed_10m") #basically response contains all the https request stuff like status code, header and finally json data
    #Connecting to the internet, Sending an HTTP GET request, Waiting for the server to respon, Receiving the response, Storing everything in response.

    our_weather_data = response.json() # we are now grabbing that particular data we needed from the request whole stuff into data dictionary i.e takes the JSON text sent by the server and converts it into a Python dictionary,

    
    return our_weather_data #data is already a Python dictionary. You don't convert it yourself. The requests library does it for you.