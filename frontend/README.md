# Personality Type Prediction - frontend

This project is a GUI application developed in Python for personality type prediction based on a user's digital activity using machine learning.

## Packages

The following packages are used in this project:

- `tkinter`: A standard Python package for creating GUI applications. It is typically included with Python installations. To check if `tkinter` is installed on your system, run the following command in the terminal or command prompt:
    ```shell
    python3 -m tkinter
    ```
    If it's not installed, you can install it using the following command:
    ```shell
    pip3 install tkinter
    ```

## Installation

1. Clone the repository:

    ```shell
    git clone https://github.com/michalbaldyga/personality-type-prediction.git
    ```

2. Navigate to the project directory:

    ```shell
    cd <paste-your-project-directory>
    ```

3. Install the required packages (if not already installed):

    ```shell
    pip3 install tkinter
    ```

## Usage

1. Run the main script to start the application:

    ```shell
    python3 main.py
    ```

- in case of "ModuleNotFoundError: No module named 'backend'", navigate to the project directory and add it to PYTHONPATH

	```shell
	export PYTHONPATH=$PWD
	```

2. The application will open `main_window.py` file.

3. To start using the app you should first click the button below the welcome text

## User Accounts

- User accounts are created and managed within the application.
- The accounts are being stored in folder called `users`, folder of each user is called by its `username`.
- Inside the folder for each user, the `password` is stored in a file `password.txt` in plain text
- You can registrate user through `Register` button

## Project Structure

- `constants.py`: This file contains constant values used throughout the project.
- `login_window.py`: This file defines the login window and its functionality.
- `main.py`: The main entry point of the application. Run this script to start the application.
- `main_app_window.py`: This file defines the main application window and its functionality.
- `main_window.py`: First window, welcome window.
- `registration_window.py`: This file defines the registration window and its functionality.
- `twitter_prediction_window.py`: In this file you can type nickname and the number of tweets for prediction.
This file is responsible for showing the results of prediction.
- `utils_front.py`: This file contains utility functions for the GUI.

## Contributing

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.


