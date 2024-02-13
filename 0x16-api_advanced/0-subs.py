#!/usr/bin/python3
"""
Function to query subscribers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers or 0 if the subreddit doesn't exist.
    """
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0

    try:
        data = response.json().get("data")
        if data and "subscribers" in data:
            return data["subscribers"]
        else:
            return 0
    except (KeyError, ValueError):
        return 0


if __name__ == "__main__":
    subreddit = raw_input("Enter subreddit name: ")  # Use raw_input for Python 2 compatibility
    subscribers = number_of_subscribers(subreddit)
    print("The subreddit '{0}' has {1} subscribers.".format(subreddit, subscribers))
