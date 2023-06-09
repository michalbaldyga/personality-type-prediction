
# Personality Type Prediction

The goal of the project is to create a tool for predicting personality type based on a user's digital activity using machine learning. In addition, it is planned to test the possibility of classifying personality type based on the user's communication style.

## How to Run the Project
To run the project, please follow the steps below:
1. Clone the repository:

    ```shell
    git clone https://github.com/michalbaldyga/personality-type-prediction.git
    ```

2. Navigate to the project directory:

    ```shell
    cd <paste-your-project-directory>
    ```

3. Install the required Python dependencies by running the following command:

    ```shell
    pip install -r requirements.txt
    ```
4. Navigate to the project's frontend directory:
   
    ```shell
    cd frontend
    ```
5. Run the main script to start the application:
 
   ```shell
   python main.py
    ```
6. The application will open `main_window.py` file.

7. To start using the app you should first click the button below the welcome text.
   
**Note**
 - In case of "ModuleNotFoundError: No module named 'backend'", navigate to the project directory and add it to PYTHONPATH

	```shell
	export PYTHONPATH=$PWD
	```
 
## Completed tasks

- [X]  Prepare autobiographies dataset and tweeter datasets
- [x]  Building scrapers/parsers
- [x]  Cleaning the data
- [x]  Creating a language model
- [x]  Training a language model
- [X]  Creating a user interface

## Documentation
- [Recent Trends in Deep Learning Based Personality Detection](https://arxiv.org/pdf/1908.03628.pdf)
 - [BERT](https://huggingface.co/docs/transformers/tasks/sequence_classification)
 - [Twitter dataset](https://www.kaggle.com/datasets/datasnaek/mbti-type)
 - [Autobiographies dataset](https://www.gutenberg.org/)

 - [MBTI Personality Types](https://www.16personalities.com/personality-types)

## Authors

- [@michalbaldyga](https://github.com/michalbaldyga)

- [@BaranskiKacper](https://github.com/BaranskiKacper)

- [@AgnieszkaDelmaczynska](https://github.com/AgnieszkaDelmaczynska)

- [@mateuszbauer](https://github.com/mateuszbauer)

- [@jakubantoszek](https://github.com/jakubantoszek)
