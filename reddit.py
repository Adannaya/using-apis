# Display the titles of the latest 10 posts in r/ShowerThoughts
# https://www.reddit.com/r/showerthoughts/new/.json?limit=10

import json
import requests

def jprint(obj):
    """Create a formatted string of the Python JSON object"""
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

url = "https://www.reddit.com/r/ShowerThoughts/new/.json"
parameters = {"limit": 10}
heads = {"User-Agent": "shower_thoughts"}
response = requests.get(url, params=parameters, headers=heads)

if response.status_code != requests.codes.ok:
    print("Page is currently unavailable, try again later.")
else:
    #jprint(response.json())
    post_titles = []
    for post in response.json():
        title = post["data"]["children"][0]["data"]["title"]
        post_titles.append(title)
    for i, post in enumerate(post_titles, start=1):
        print(f"{i}: {post}")