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
    # Output: True
    subreddit_search = input("Enter subreddit to search: ")
    for submission in reddit.subreddit(subreddit_search).hot(limit=10):
        print(submission.title)
if __name__ == "__main__":
    main()
