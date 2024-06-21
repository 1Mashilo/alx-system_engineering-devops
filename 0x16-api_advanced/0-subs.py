#!/usr/bin/python3
"""
Uses Reddit API to print the number of subscribers of a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit.
    If the subreddit is invalid, return 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'myAPI/0.0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    try:
        data = response.json().get("data")
        return data.get("subscribers", 0)
    except (ValueError, AttributeError):
        return 0