import os

from transformers import pipeline
from user_input import get_input_from_user, get_tweets


def _get_path_to_model():
    path = os.path.join(os.path.dirname(__file__), 'model')
    return path if os.path.isdir(path) else os.path.join(os.path.dirname(__file__), 'release', 'model')


try:
    classifier = pipeline(
        "text-classification",
        model=_get_path_to_model(),
        tokenizer="distilbert-base-uncased",
        framework="pt", top_k=16)
except OSError:
    classifier = None


def predict(text: str):
    if classifier is not None:
        # split text to batches of 512 tokens
        batch_size = 512
        batches = [text[i:i + batch_size] for i in range(0, len(text), batch_size)]

        # predict
        predictions = {}
        for batch in batches:
            result = classifier(batch, padding=True)
            for res in result[0]:
                predictions[res['label']] = predictions.get(res['label'], 0) + res['score']

        # get the best three as a list of personality types
        best_predictions = sorted(predictions.items(), key=lambda item: item[1], reverse=True)[0:3]
        best_predictions_list = []
        for prediction in best_predictions:
            best_predictions_list.append(str(prediction[0]))

        return best_predictions_list
    else:
        return None
