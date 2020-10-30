# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:28:17 2020

@author: truet
"""
import praw
from bs4 import BeautifulSoup as bs
import requests

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
        url = "https://old.reddit.com/r/ScottishPeopleTwitter/comments/ji0s78/she_was_lucky/"
        submission = reddit.submission(url=url)
        return submission


    def store_usernames(self):
        submission = self.retrieve_usernames()
        all_comments = submission.comments.list()
        usernames = {str(comment.author) for comment in all_comments}
        return usernames
    
    
    def scrape_analyser(self):
        







PoliticsStatistics().store_usernames()


