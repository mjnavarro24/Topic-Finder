import praw #This module is used to create Reddit instances
import json

def create_reddit_instance(read_only = False):
    credentials = None
    with open('credentials.json') as creds:
        credentials = json.load(creds)

    if(not read_only):
        reddit_instance = praw.Reddit(client_id = credentials['client_id'],
                                        client_secret = credentials['client_secret'],
                                        username = credentials['username'],
                                        password = credentials['password'],
                                        user_agent = credentials['user_agent'])

    else:
        reddit_instance = praw.Reddit(client_id = credentials['client_id'],
                                        client_secret = credentials['client_secret'],
                                        user_agent = credentials['user_agent'])
    return reddit_instance

def search_suball_week(searchword):
    reddit_instance = create_reddit_instance(read_only=True)
    subreddit = reddit_instance.subreddit('all')
    list_keyword = []
    for post in subreddit.search(query=searchword, sort='top', time_filter='week'):
        list_keyword.append(post.title)

    list_common_words = {}
    for title in list_keyword:
        for word in title.split():
            word = word.replace(',', '')
            word = word.replace('.','')
            word = word.replace('\'','')
            if len(word.lower()) > 4:
                if not word_in_search(word, searchword) or word == "would" or word == "would" or word == "should" or word == "about" or word == "after" or word == "because":
                    pass
                elif word in list_common_words:
                    list_common_words[word] += 1
                else:
                    list_common_words[word] = 1
    list_top_similar_words = {}

    for key in list_common_words:
        if list_common_words[key] >= 3:
            list_top_similar_words[key] = list_common_words[key]
    sim_words = "Common words associated with your search: "
    for key in list_top_similar_words.keys():
        sim_words += str(key) + ", "
    list_keyword = list_keyword[0:10]
    list_keyword.append(sim_words)
    return list_keyword

def word_in_search(word: str, searchwords) -> bool:
    not_in_search = True
    word_list = searchwords.split()
    for a in word_list:
        if a in word:
            not_in_search = False
    return not_in_search