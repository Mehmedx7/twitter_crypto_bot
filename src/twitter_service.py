import requests
from bs4 import BeautifulSoup

def get_latest_tweet(username):
    try:
        url = f"https://nitter.net/{username}"        
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")

        tweet = soup.find("div", class_="tweet-content")
        if tweet:
            return tweet.text.strip()
        else:
            return None
    except Exception as e:
        print(f"An error occurred while fetching the tweet: {e}")
        return None