# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:28:17 2020

@author: truet
"""
import praw
from collections import Counter
from multiprocessing import Process, Queue
from multiprocessing.dummy import Pool
import sys

users_data = {}

def credentials():
    reddit = praw.Reddit(
        client_id="regAkCxBDMi1fw",
        client_secret="cwEIsCDiQeZAmFskRU9iRLOF51s",
        user_agent="windows:politicalbreakdownbot:v1.0.0 (by /u/XXXXX)"
        )
    return reddit


def retrieve_usernames():
    reddit = credentials()
    #test url
    url = "https://old.reddit.com/r/ScottishPeopleTwitter/comments/ji0s78/she_was_lucky/"
    submission = reddit.submission(url=url)
    return submission


def store_usernames():
    submission = retrieve_usernames()
    all_comments = submission.comments.list()
    usernames = []
    for comment in all_comments:
        if str(comment.author) not in usernames:
            usernames.append(str(comment.author))
    if len(usernames) > 100:
        usernames = usernames[:100]
    return usernames


def users_top_10(username):
    client = credentials()
    user = praw.reddit.Redditor(client, username)
    history = [post.subreddit.display_name for post in user.new(limit=None)]
    counts = Counter(history).most_common(12)
    counts = [item[0].lower() for item in counts[2:]]
    users_data[username] = counts
    
    
        
if __name__ == "__main__":

    pool = Pool(50)
    results = [pool.apply_async(users_top_10, (user,)) for user in store_usernames()]
    pool.close()
    pool.join()
    print(users_data)

            











