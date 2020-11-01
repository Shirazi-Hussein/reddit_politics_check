# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:28:17 2020

@author: truet
"""
import praw
import subreddit_list
from collections import Counter


class PoliticsStatistics:
    
    
    def credentials(self):
        reddit = praw.Reddit(
            client_id="regAkCxBDMi1fw",
            client_secret="cwEIsCDiQeZAmFskRU9iRLOF51s",
            user_agent="my user agent"
            )
        return reddit


    def retrieve_usernames(self):
        reddit = self.credentials()
        #test url
        url = "https://old.reddit.com/r/ScottishPeopleTwitter/comments/ji0s78/she_was_lucky/"
        submission = reddit.submission(url=url)
        return submission


    def store_usernames(self):
        submission = self.retrieve_usernames()
        all_comments = submission.comments.list()
        usernames = {str(comment.author) for comment in all_comments}
        return usernames
    
    
    def users_top_10(self):
        client = self.credentials()
        usernames = self.store_usernames()
        user_data = []
        for username in usernames:
            user = praw.reddit.Redditor(client, username)
            history = [post.subreddit.display_name for post in user.new(limit=None)]
            counts = Counter(history).most_common(10)
            user_data.append({username:dict(counts)})
        

t = PoliticsStatistics()
print(len(t.store_usernames()))
            











