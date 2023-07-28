# Reddit-Search-Bot
Reddit bot searches reddit for user specified keywords on user specified subreddits using the PRAW library.

The client_id, client_secret are provided by Reddit on creating a developer account and user_agent is an unique name used in-case the bot starts to malfunction.

The reddit.read_only returns True if the connection with Reddit happens succesfully. Otherwise it returns False and we would need to check whether the client id, client secret or user agent were input correctly or not.
The subreddit_name defines the name of the subreddit and the search_item gives us the keyword.
If the keyword is found, the program will return the Title and the Link.
