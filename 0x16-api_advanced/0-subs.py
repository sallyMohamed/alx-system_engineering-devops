#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json().get("data")
        if data:
            subscribers = data.get("subscribers")
            if subscribers is not None:
                return subscribers
    
    return 0
