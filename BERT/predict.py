from transformers import pipeline
from user_input import get_input_from_user, get_tweets


classifier = pipeline("text-classification", model="../model", tokenizer="distilbert-base-uncased",
                      framework="pt", top_k=16)


def predict(text: str):
    # split text to batches of 512 tokens
    batch_size = 512
    batches = [text[i:i+batch_size] for i in range(0, len(text), batch_size)]

    # predict
    predictions = {}
    for batch in batches:
        result = classifier(batch, padding=True)
        for res in result[0]:
            predictions[res['label']] = predictions.get(res['label'], 0) + res['score']

    print(sorted(predictions.items(), key=lambda item: item[1], reverse=True))


account_name, number_of_tweets = get_input_from_user()
if number_of_tweets <= 0:
    print('Wrong data typed')
else:
    tweets_content = get_tweets(account_name, number_of_tweets)
    if tweets_content != '':
        predict(tweets_content)
    else:
        print("Account doesn't exist or have no Tweets")
