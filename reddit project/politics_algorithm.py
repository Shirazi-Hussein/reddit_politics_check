import subreddit_list
import re

def match(li1, li2):
    similar = set(li1) & set(li2)
    return len(similar)

def affiliation(users_data):
    for user, subs in users_data.items():
        conservative = match(subreddit_list.right_subs, subs)
        liberal = match(subreddit_list.left_subs, subs)
        if conservative > liberal:
            users_data[user].append('csrv')
        elif liberal > conservative:
            users_data[user].append('lbrl')
        elif liberal == conservative:
            users_data[user].append('undtrmd')

def return_count(users_data):
    users_data = str(users_data)
    conservative_pct = len(re.findall('csrv', users_data))
    liberal_pct = len(re.findall('lbrl', users_data))
    undetermined_pct = len(re.findall('undtrmd', users_data))
    data = [conservative_pct, liberal_pct, undetermined_pct]
    return data



