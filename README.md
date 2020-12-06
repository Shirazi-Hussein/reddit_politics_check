# About
With politics and partisan issues being a hotspot for both news and social media alike, I created an app that takes any reddit thread and returns a graph of how many commenters 
lean towards a specific demographic ("right-leaning", "left-leaning", and "not determined"). I feel like having total transparency with the insivisble bias that are hosted in every 
news thread is productive to help open up views on either side, and moreso create a healthier atmosphere for argument.

# Built With
- Selenium
- PRAW
- MatPlotLib

# Getting Started
1. PRAW requires user credentials, which are needed in `redditdata.py`
2. Install Matplotlib.
3. Enter the reddit thread to be examined in the url variable found in `redditdata.py`.

# Usage
The algorithm works on a point system; `subreddit_list.py` contains both a list of subreddits that are viewed as left leaning and another for subreddits viewed as right leaning.
If a user has a subreddit from either list in their most-active subreddits, then a counter goes up for that bias. For example, if a user was active enough in r/conservative,
then the `conservative` counter goes up by 1. On the other hand, if a user was active enough on a subreddit like r/voteblue, then the `liberal` counter goes up by 1.
Whichever counter is larger is what determines a users bias. If there isnt enough data to make a reading, the return result is `undetermined`.
