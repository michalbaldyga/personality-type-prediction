import os
from transformers import pipeline
import pandas as pd
from tqdm import tqdm


def _get_path_to_model():
    path = os.path.join(os.path.dirname(__file__), 'model')
    return path if os.path.isdir(path) else os.path.join(os.path.dirname(__file__), 'release', 'model')


def test_model():
    """Calculate model accuracy on the test dataset."""

    # Read test dataset
    df = pd.read_csv('../datasets/tweets_test.csv', delimiter='|')

    # Initialize accuracy variables
    correct, total = 0, len(df)

    # Initialize the classifier
    classifier = pipeline(
        "text-classification",
        model=_get_path_to_model(),
        tokenizer="distilbert-base-uncased",
        framework="pt")

    # Iterate over each example in the test dataset
    for i in tqdm(range(total)):
        # Get text and label for current example
        text = df['text'][i]
        label = df['label'][i]

        # Make a prediction using the classifier
        guess = classifier(text)[0]['label']

        # Check if the predicted label matches the true label
        if label == guess:
            correct += 1

    # Calculate accuracy as the ratio of correct predictions to total examples
    accuracy = correct / total
    return accuracy


print(f"Accuracy: {test_model()}")
