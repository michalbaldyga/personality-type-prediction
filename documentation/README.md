# System Documentation
## Introduction 
This documentation provides an overview of the components used in the system, as well as the datasets and classification process. The system utilizes the BERT model from Hugging Face for MBTI (Myers-Briggs Type Indicator) classification. The following sections explain each component in detail.
## MBTI Model
The MBTI model is a machine learning model that predicts the personality type of an individual based on the Myers-Briggs Type Indicator framework. It categorizes individuals into one of sixteen personality types, such as INTJ, ENFP, etc. The model is trained using the BERT (Bidirectional Encoder Representations from Transformers) architecture, which is a state-of-the-art natural language processing model.
 

It consists of four **dimensions**, each represented by two opposing traits:

- E (Extraversion) vs. I (Introversion)
- S (Sensing) vs. N (Intuition)
- T (Thinking) vs. F (Feeling)
- J (Judging) vs. P (Perceiving)


By combining these dimensions, a total of **16** different **personality types** can be identified.

## Datasets
To prepare the datasets for training and evaluation, the following data sources were utilized:

- 78 autobiographies
- 101 Twitter accounts with 1,000 tweets each
- One ready-made collection from Kaggle
Each autobiography and Twitter account belongs to a person with a known personality type. The combined dataset consists of text samples from diverse individuals, enabling the model to learn patterns associated with different personality types.

The following steps were executed to prepare the data:

1. **Data Collection**: We gathered posts containing MBTI types from various online communities.

    2. **Preprocessing**: The text data was cleaned by removing irrelevant content, such as URLs and special characters.
    3. **Feature Extraction**: We extracted relevant features from the text, including word frequencies and sentiment analysis scores.



More info is included in  ```README.md ``` placed in *datasets* directory.

## System Components
The system consists of the following components:

- Machine Learning Model: BERT-based MBTI classifier
- Desktop Application: Graphical user interface (GUI) for interacting with the model
The libraries used in the system, along with their versions, are as follows:
### Backend:
#### Training & predicting  **model**:
- transformers (version 4.29.2): Provides the BERT model and related utilities.
- xformers (version 0.0.20): Library for model interpretation and analysis.
- datasets (version 2.12.0): Provides access to the datasets and data preprocessing capabilities.
- evaluate (version 0.4.0): Package for evaluating the model's performance.
- scikit-learn (version 1.2.2): Used for additional data preprocessing and evaluation tasks.
- torch (version 1.9.0): PyTorch library for deep learning.
- torchvision (version 0.10.0): Provides computer vision utilities for image-related tasks.
- torchaudio (version 0.9.0): Library for audio-related tasks.
- snscrape (version https://github.com/JustAnotherArchivist/snscrape.git@c3b216c3cb8593513a018eb3ec4fd6f18d3aba5b): GitHub repository for scraping Twitter data.
- accelerate (version 0.20.3): Library for distributed training and optimization.
The chosen libraries were selected based on their popularity, community support, and compatibility with the BERT model and overall system requirements.
#### Preparing & cleaning **data**:
- pypdf2 (version 3.0.1): Library for working with PDF files in Python.
- regex (version 2023.5.5): : Library for regular expression matching and manipulation.
- pandas (version 2.0.2): For manipulating the csv files.
- csv (version 3.8.0 ) Fast CSV Parser for Python.

### Frontend
- tkinter (version 3.11.4): Library for creating GUI applications.

## Classification Process
The classification process involves predicting the entire personality type using the BERT-based MBTI model. The model assigns one of sixteen classes to each input sample. The classification is performed by feeding the preprocessed text data through the BERT model, which encodes the text into contextualized representations. These representations are then passed through additional layers to obtain the final classification results.

## Results
||                Tweets|Autobiographies|Tweets + Autobiographies|
| ---------------------| ------ | ----- | -----------------------|
| 4 **dimensions** correct | 7.73%  | 5.37% | 8.81%                  |
| 3+ **dimensions** correct| 28.92% | 32.19%| 29.93%                 |

#### First row: 
1 point for the proper prediction.

#### Second row:
 0.75 point for 3 proper dimensions & 1 point for the proper prediction.

## Conclusions
Based on the results, the accuracy of the MBTI classification using the BERT model is average. The model performs better in predicting three or more correct letters compared to predicting all four letters accurately. With the knowledge gained from this project, several **improvements** could be made. Some potential changes include:

- Increasing the size and diversity of the training dataset
- Exploring alternative pretraining methods for BERT
- Fine-tuning hyperparameters and conducting a more extensive search
The **most challenging** aspect of the project was obtaining and preprocessing the data from multiple sources. Collecting the autobiographies, scraping tweets, and integrating the Kaggle dataset required significant effort and attention to detail.

The **time-consuming** tasks in the project included training the BERT model on a large-scale dataset, optimizing the model's performance, and fine-tuning various parameters to achieve satisfactory results.

While the results are not ideal, they provide valuable insights and form the basis for further research and improvements.