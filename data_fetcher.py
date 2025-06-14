import praw
import re

def fetch_and_clean_data():
    
    reddit = praw.Reddit(
        client_id
        client_secret
        user_agent
    )

   
    subreddit = reddit.subreddit("UnKnoWnCheaTs") 
    with open("elden_ring_cheats_data.txt", "w", encoding="utf-8") as file:
        for post in subreddit.hot(limit=10):  
            file.write(post.title + " " + post.selftext + "\n")

   
    with open("elden_ring_cheats_data.txt", "r", encoding="utf-8") as file:
        data = file.readlines()

    cleaned_data = [re.sub(r"http\S+|www\S+|[^a-zA-Z\s]", "", post.lower()) for post in data if "cheat" in post or "hack" in post]

    with open("cleaned_elden_ring_cheats_data.txt", "w", encoding="utf-8") as file:
        for post in cleaned_data:
            file.write(post + "\n")
    print("Data fetched and cleaned successfully.")
