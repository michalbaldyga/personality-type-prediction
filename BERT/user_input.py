# pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git
import snscrape.modules.twitter as sntwitter
import re


def clean_tweet(tweet):
    return tweet


def get_input_from_user():
    print('Type account name: ')
    username = input()

    print('Type number of Tweets: ')
    no_of_tweets = input()

    try:
        tweets_number = int(no_of_tweets)
        return username, tweets_number
    except ValueError:
        return username, -1


def get_tweets(username, no_of_tweets):
    text = ''

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper('from:' + username).get_items()):
        if i > no_of_tweets:
            break

        text += clean_tweet([tweet.rawContent][0]) + '. '

    return text
