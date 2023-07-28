import praw

def main():
    # Reddit API credentials (replace with your own)
    client_id = ""
    client_secret = ""
    user_agent = ""

    # Create a Reddit instance
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent,
    )
    print(reddit.read_only)

    subreddit_name = input("Enter name of the Subreddit: ")
    subreddit = reddit.subreddit(subreddit_name)
    search_item=input("Term to search for: ")

    print(f"Bot is monitoring r/{subreddit_name} subreddit for posts with the keyword {search_item}...")

    # Start monitoring
    for submission in subreddit.stream.submissions():
        if search_item in submission.title.lower():
            print(f"\nFound a useful tutorial post:")
            print(f"Title: {submission.title}")
            print(f"Link: {submission.url}")

if __name__ == "__main__":
    main()
