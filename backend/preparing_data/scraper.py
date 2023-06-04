import os
import snscrape.modules.twitter as sntwitter
import pandas as pd

from clear import clear_data

accounts = {
    'ENTP': ['BarackObama', 'newtgingrich', 'jonstewart', 'JeremyClarkson', 'OfficalMrBean', 'salmahayek', 'GillianA'],

    'INTP': ['jimmy_wales', 'PaulGAllen', 'Plaid_Page', 'Plaid_Brin', 'BenStein1944'],

    'ENTJ': ['BillGates', 'SpeakerPelosi', 'JebBush', 'Adele', 'CobieSmulders'],

    'INTJ': ['elonmusk', 'paulkrugman', 'Schwarzenegger', 'rogerwaters', 'HillaryClinton'],

    'ENFP': ['justinbieber', 'RalphNader', 'SalmanRushdie', 'ariannahuff', 'katiecouric', 'TheEllenShow',
             'shailenewoodley', 'HansZimmer'],

    'INFP': ['jk_rowling', 'bjork', 'hughlaurie', 'florencemachine', 'AoDespair', 'respektor', 'StephenAtHome'],

    'ENFJ': ['katyperry', 'ddlovato', 'Oprah', 'Drake', 'MatthieuRicard', 'charlierose'],

    'INFJ': ['adrienbrody', 'EdwardNorton', 'DavidSchwimmer', 'JoshRadnor', 'DerrenBrown'],

    'ESTJ': ['HillaryClinton', 'MichelleObama', 'EmmaWatson', 'AnnCoulter', 'BillOReilly', 'megynkelly',
             'ebertchicago'],

    'ISTJ': ['Nick_Offerman', 'RiversCuomo', 'danicamckellar', 'morgan_freeman', 'Ayaan'],

    'ESFJ': ['JLo', 'SarahPalinUSA', 'jes_chastain', 'victoriabeckham', 'selenagomez', 'MariahCarey', 'ShaniaTwain',
             'RealHughJackman'],

    'ISFJ': ['KimKardashian', 'kendricklamar', 'DrBrianMay', 'AnthonyHopkins', 'halleberry', 'GwynethPaltrow'],

    'ESTP': ['NiallOfficial', 'realDonaldTrump', 'Madonna', 'KevinSpacey', 'BenAffleck', 'RyanSeacrest',
             'taylorswift13', 'MillaJovovich'],

    'ISTP': ['narendramodi', 'MagnusCarlsen', 'justdemi', 'AnnaKendrick47', 'RonPaul', 'TomCruise', 'TheElliotPage'],

    'ESFP': ['Cristiano', 'neymarjr', 'shakira', 'MileyCyrus', 'BrunoMars', 'KylieJenner', 'HowardSchultz',
             'TonyRobbins'],

    'ISFP': ['rihanna', 'jtimberlake', 'ladygaga', 'RyanGosling', 'aMonicaBellucci', 'xtina', 'leonalewis',
             'DrewBarrymore', 'pamelaanderson']}

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
            'Personality Type': personality_types,
            'Tweets': clear_tweets
        }
        # Creating a dataframe from the tweets list above
        tweets_df = pd.DataFrame(data=data)

        tweets_df.to_csv('Tweets/' + key + '/' + account_name + '.csv', sep=';', index=False)

