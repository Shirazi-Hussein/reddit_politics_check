# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:28:17 2020

@author: truet
"""
import praw
from praw.models import MoreComments
from collections import Counter
from multiprocessing import Process, Queue
from multiprocessing.dummy import Pool
import politics_algorithm
import graph

users_data = {}

def credentials():
    reddit = praw.Reddit(
        client_id="RC76UTAhiJSqpA",
        client_secret="UhuYXtZmt7VXXqpz0wNq8FZTzCtKAA",
        user_agent="windows:politicalbreakdownbot:v1.0.0 (by /u/God_i_hate_today)"
        )
    return reddit


def retrieve_usernames():
    reddit = credentials()
    #test url
    url = "https://old.reddit.com/r/Conservative/comments/jnc7am/illinois/"
    submission = reddit.submission(url=url)
    return submission


def store_usernames():
    submission = retrieve_usernames()
    usernames = []
    submission.comments.replace_more(limit=0)
    for top_level_comment in submission.comments:
        if str(top_level_comment.author) not in usernames:
             usernames.append(str(top_level_comment.author))
    if len(usernames) > 100:
        usernames = usernames[:100]
    return usernames


def users_top_10(username):
    client = credentials()
    user = praw.reddit.Redditor(client, username)
    history = [post.subreddit.display_name for post in user.new(limit=None)]
    counts = Counter(history).most_common(22)
    counts = [item[0].lower() for item in counts[2:]]
    users_data[username] = counts
    
    
        
if __name__ == "__main__":

    pool = Pool(50)
    results = [pool.apply_async(users_top_10, (user,)) for user in store_usernames()]
    pool.close()
    pool.join()
    
    politics_algorithm.affiliation(users_data)
    data = politics_algorithm.return_count(users_data)
    graph.plot_data(data)
    
            











