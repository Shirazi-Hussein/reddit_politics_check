import subreddit_list



def match(li1, li2):
    similar = set(li1) & set(li2)
    return len(similar)

def politics_algorithm(user_data):
    #grab each username
    conservative = match(subreddit_list.right_subs, subs)
    liberal = match(subreddit_list.left_subs, subs)
    if conservative > liberal:
        #add "conservative" to the user_data
        temp2.append(user_data, 'conservative')
    elif liberal > conservative:
        #add "liberal" to the user_data     
        temp2.append(user_data, 'liberal')
    elif liberal == conservative:
        #add "undetermined" to the user_data
        temp2.append(user_data, 'undetermined')

\
