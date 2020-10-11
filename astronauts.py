# Taken from https://www.dataquest.io/blog/python-api-tutorial

import json
import requests
from datetime import datetime


def jprint(obj):
    """Create a formatted string of the Python JSON object"""
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


# We want to find out how many astronauts are in space right now
response = requests.get("http://api.open-notify.org/astros.json")

if response.status_code != 200:
    print("Page not found!")
    print("It seems http://api.open-notify.org/astros.json is unavailable right now.")
else:
    jprint(response.json())

# Co-ordinates so we can see when the ISS will
# pass over the Empire State Building
parameters = {
    "lat": 40.748817,
    "lon": -73.985428
}

# By adding the keyword argument params to our request, we don't have to
# worry about inserting the values into the URL string
response = requests.get(
    "http://api.open-notify.org/iss-pass.json", params=parameters)

if response.status_code != 200:
    print("Page not found!")
    print("It seems http://api.open-notify.org/iss-pass.json is unavailable right now.")
else:
    # jprint(response.json())
    pass_times = response.json()["response"]
    # jprint(pass_times)

    # Collect all the times the ISS will
    # pass over our address into a list
    risetimes = []
    for x in pass_times:
        time = x["risetime"]
        risetimes.append(time)

    # Convert pass times from epoch format to
    # human-readable format
    times = []
    for rt in risetimes:
        time = datetime.fromtimestamp(rt)
        times.append(time)
        print(time)
