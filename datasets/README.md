
# Datasets

To prepare these datasets, we collected **78 autobiographies** , **101 twitter accounts** with 1,000 tweets from each, and used one **ready-made collection** from kaggle. Each person whose autobiography or account we used has a known personality type.


| label         | text          | 
| ------------- | ------------- | 
| ENFJ          |  We are not born for ourselves alone.     | 
| ENFJ          | A friend is a second self.         | 
| ENFJ          | In anger nothing judicious can be done.     | 
| ENFJ          | They say that if God spoke Greek, he would speak like Plato.         | 
|.|.|
|.|.|
|.|.|







## Description

- **dataset_autobiographies.csv**: Autobiographies obtained mainly from three parties were used to  create this dataset:
    - https://www.gutenberg.org/
    - https://openlibrary.org/
    - https://www.pdfdrive.com/
    It contains 28595 lines, and each line has a maximum of        512 characters
- **dataset_twitter.csv**: Ready-made collection from kaggle:
    - https://www.kaggle.com/datasets/datasnaek/mbti-type
    It contains 3024 lines, and each line contains a section of each of the last 50 things that PersonalityCafe forum users have posted (each entry separated by "||" (3 pipe characters)).
- **dataset_twitter1.csv**, **dataset_twitter2.csv** : Tweets obtained from the most popular accounts according to the site:
    - https://en.wikipedia.org/wiki/List_of_most-followed_Twitter_accounts
    The difference between the sets of :
    - **dataset_twitter1.csv** does not have **hashtags**, **usernames** in tweets and **emoticons**
    It contains 88936 lines, and each line has one tweet.

    - **dataset_twitter2.csv**, on the other hand, has only been cleared of **links**

    It contains 90821 lines, and each line has one tweet.
    

## Acknowledgements

Websites based on which we determined the user's personality type:
 - [IDRlabs](https://www.idrlabs.com/)
 - [personality-database](https://www.personality-database.com/)



## License

[MIT](https://choosealicense.com/licenses/mit/)

