#!/usr/bin/python3
"""
Function to query subscribers on a given Reddit subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers on a given subreddit.

    Handles potential errors by checking the status code and JSON decoding.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0  # Handle non-existent subreddits gracefully

    try:
        # Improved JSON decoding with proper error handling
        data = response.json()
        results = data.get("data")
        return results.get("subscribers", 0)  # Default to 0 for missing data
    except (requests.exceptions.JSONDecodeError, KeyError) as e:
        print(f"Error: Failed to decode JSON or missing data - {e}")
        return 0

# Example usage (uncomment for testing)
# subreddit = "programming"
# subscribers = number_of_subscribers(subreddit)
# print(f"Subscribers for '{subreddit}': {subscribers}")
