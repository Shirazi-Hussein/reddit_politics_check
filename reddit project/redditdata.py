# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:28:17 2020

@author: truet
"""
import praw
import subreddit_list
from collections import Counter
from multiprocessing import Process



class PoliticsStatistics:
    
    
    def credentials(self):
        reddit = praw.Reddit(
            client_id="regAkCxBDMi1fw",
            client_secret="cwEIsCDiQeZAmFskRU9iRLOF51s",
            user_agent="windows:politicalbreakdownbot:v1.0.0 (by /u/God_i_hate_today)"
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
        usernames = list(usernames)
        if len(usernames) > 100:
            usernames = usernames[:100]
        return usernames
    
    
    def users_top_10(self, username):
        client = self.credentials()
        global user_data
        user_data = []
        user = praw.reddit.Redditor(client, username)
        history = [post.subreddit.display_name for post in user.new(limit=None)]
        counts = Counter(history).most_common(10)
        counts = [item[0] for item in counts[2:]]
        user_data.append({username:counts})
        
#test
if __name__ == "__main__":
    t = PoliticsStatistics()
# =============================================================================
#     for username in t.store_usernames():
#         p = Process(target=t.users_top_10, args=(username,))
#         p.start()
#         p.join()
#     print("completed")
# =============================================================================
    for username in t.store_usernames():
        t.users_top_10(username)
        print('done')
    print('--------------------completed job----------------------------------')
        


            











