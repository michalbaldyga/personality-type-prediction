
# MBTI Prediction using BERT

The BERT model was proposed in BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding by Jacob Devlin, Ming-Wei Chang, Kenton Lee and Kristina Toutanova. It’s a bidirectional transformer pretrained using a combination of masked language modeling objective and next sentence prediction on a large corpus comprising the Toronto Book Corpus and Wikipedia.


## Packages

The following packages are used in this project:

- `transformers`: Powerful library for natural language processing tasks, especially in the field of transformer-based models like BERT.
- `datasets`: Versatile package that provides easy access to various publicly available datasets for machine learning and data analysis.
- `evaluate`: Package that offers convenient functions and tools for evaluating the performance and quality of machine learning models.
- `scikit-learn`: Comprehensive library for machine learning that provides a wide range of tools and algorithms for data preprocessing, modeling, and evaluation.
- `snscrape`: Package for scraping data from social media platforms like Twitter, enabling the collection of specific information for analysis or research purposes.
- `pytorch`: Popular open-source machine learning library that provides a flexible framework for building and training neural networks, particularly well-suited for deep learning tasks.
- `accelerate`: Library that simplifies distributed training and optimization of PyTorch models, allowing for efficient parallel processing across multiple GPUs or machines.
- `xformers`: Library that allows using `memorry_efficient_attention` to accelerate training.

## Project Structure

- `user_input.py`: A Python script that facilitates the scraping of tweets from a specific person specified by the user, allowing for data collection from social media for further analysis or processing.
- `clear_tweets.py`: A Python script responsible for cleaning and preprocessing the scraped text data, which involves removing noise, filtering out irrelevant information, and standardizing the text format to ensure consistency and enhance the quality of the subsequent analysis.
- `train.py`: A Python script that takes a dataset and trains a BERT (Bidirectional Encoder Representations from Transformers) model, leveraging its powerful natural language processing capabilities to learn patterns and features from the input data, typically for tasks such as text classification or sentiment analysis.
- `predict.py`: A Python script that utilizes a trained BERT model to make predictions on new or unseen data, specifically targeting the task of personality type prediction, where the model takes input text and determines the corresponding personality type based on the learned patterns.
- `test.py`: A Python script designed to assess the accuracy and performance of a trained model by applying it to a separate test dataset, enabling the evaluation of how well the model generalizes to unseen data and providing insights into its effectiveness for the specific task at hand.

## Folders

- `preparing_data`: Contains various scripts related to parsing and preparing data
- `release`: Contains trained model which will be used by default
- `train_model`: Contains a script used for training model by a user alone


## Training

In order to train the model, head to `train_model` directory and run `train.py`

```bash
  cd backend/train_model/
  python3 train.py
```

The model will be saved in the `backend/model` directory and will be used instead of the one in `backend/release/model`

## Testing

In order to see the accuracy and performance of the trained model run Python script `test.py`

```bash
  python3 test.py
```

After the tests have been carried out, the results of the model output will be returned.

## Documentation

https://huggingface.co/docs/transformers/tasks/sequence_classification

## License

[MIT](https://choosealicense.com/licenses/mit/)

