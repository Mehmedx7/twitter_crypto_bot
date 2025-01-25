from src.twitter_service import get_latest_tweet

def main():
    username = "elonmusk"  # Replace with the target username
    latest_tweet = get_latest_tweet(username)
    
    if latest_tweet:
        print(f"Latest tweet from @{username}: {latest_tweet}")
    else:
        print(f"No tweets found for @{username} or all Nitter instances failed.")

if __name__ == "__main__":
    main()