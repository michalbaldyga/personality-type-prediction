import pandas as pd
import os


def merge_data(folder_path):
    for root, directories, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            #  Read the CSV file into a DataFrame
            data = pd.read_csv(file_path, sep='|')
            # Append the data to the merged_data DataFrame
            data.to_csv('tweets.csv', mode='a', sep='|', index=False, header=False)


merge_data('Tweets2\Tweets')
