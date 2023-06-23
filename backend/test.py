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
    df = df.dropna()  # Remove all None rows

    # Initialize accuracy variables
    correct, total = 0., 22780

    # Initialize the classifier
    classifier = pipeline(
        "text-classification",
        model=_get_path_to_model(),
        tokenizer="distilbert-base-uncased",
        framework="pt")

    # Iterate over each example in the test dataset
    for i in tqdm(range(total)):
        # Get text and label for current example
        text = str(df['text'][i])
        label = df['label'][i]

        # Make a prediction using the classifier
        guess = classifier(text)[0]['label']

        # Check if the predicted label matches the true label
        correct_letters = 0

        for j in range(len(label)):
            if guess[j] == label[j]:
                correct_letters += 1

        if correct_letters == 3:
            correct += 0.75
        elif correct_letters == 4:
            correct += 1.0

    # Calculate accuracy as the ratio of correct predictions to total examples
    accuracy = correct / total
    return accuracy


print(f"Accuracy: {test_model()}")
