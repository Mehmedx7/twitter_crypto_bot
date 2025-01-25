import snscrape.modules.twitter as sntwitter


def get_latest_tweet(username):
    try:
        tweets = sntwitter.TwitterUserScraper(username).get_items()
        latest_tweet = next(tweets)
        return latest_tweet.content
    except Exception as e:
        return f"Error fetching tweet: {e}"