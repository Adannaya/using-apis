# Display the titles of the latest 10 posts in r/ShowerThoughts
# https://www.reddit.com/r/showerthoughts/new/.json?limit=10

import json
import requests

def jprint(obj):
    """Create a formatted string of the Python JSON object"""
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
