import os
import snscrape.modules.twitter as sntwitter
import pandas as pd

from backend.clear_tweets import clear_data
from backend.preparing_data.merge import merge_data

accounts = {
    'ENTP': ['BarackObama', 'newtgingrich'],

    'INTP': ['jimmy_wales', 'PaulGAllen'],

    'ENTJ': ['BillGates', 'SpeakerPelosi'],

    'INTJ': ['elonmusk', 'paulkrugman'],

    'ENFP': ['RalphNader', 'SalmanRushdie'],

    'INFP': ['jk_rowling', 'bjork'],

    'ENFJ': ['katyperry', 'ddlovato'],

    'INFJ': ['adrienbrody', 'EdwardNorton'],

    'ESTJ': ['HillaryClinton', 'MichelleObama'],

    'ISTJ': ['Nick_Offerman', 'RiversCuomo'],

    'ESFJ': ['JLo', 'SarahPalinUSA'],

    'ISFJ': ['KimKardashian', 'kendricklamar'],

    'ESTP': ['NiallOfficial', 'Madonna'],

    'ISTP': ['narendramodi', 'MagnusCarlsen'],

    'ESFP': ['Cristiano', 'neymarjr'],

    'ISFP': ['rihanna', 'RyanGosling']
}

os.makedirs('Tweets/', exist_ok=True)
for key in accounts:
    os.makedirs('Tweets/' + key + '/', exist_ok=True)

# enter no of tweets
no_of_tweets = 1000

for key, value in accounts.items():
    for account_name in value:
        clear_tweets = []
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper('from:' + account_name).get_items()):
            if i > no_of_tweets:
                break
            clear_tweet = clear_data(tweet.rawContent)

            if len(clear_tweet) != 1:
                clear_tweets.append(clear_tweet)

        personality_types = [key] * len(clear_tweets)

        data = {
            'label': personality_types,
            'text': clear_tweets
        }
        # Creating a dataframe from the tweets list above
        tweets_df = pd.DataFrame(data=data)

        tweets_df.to_csv('Tweets/' + key + '/' + account_name + '.csv', sep='|', index=False)

merge_data('Tweets')
