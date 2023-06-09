# Personality Type Prediction - frontend

This project is a Python-based GUI application that utilizes machine learning to predict a user's personality type based on their digital activity. The application provides a graphical user interface for users to interact with and input their digital data for analysis. Using advanced machine learning algorithms, the application processes the input data and generates predictions about the user's personality type.

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

## License

[MIT](https://choosealicense.com/licenses/mit/)
