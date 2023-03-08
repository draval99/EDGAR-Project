
import pandas as pd

def write_document_sentiments(input_folder : str, output_file : str):
    '''
    Takes a folder with cleaned html files and outputs a
    dataframe of word sentiments for each year
    '''

    data = []
    ## just a note for when you get round to this - I need a way to call the filename strings later in the code so if you have a way to do that I would appreciate it
    for file in input_folder:
        sentiment_data = file.get_sentiment_word_dict() # Part 3C function - Outputs dictionary of word sentiments
        data.append(sentiment_data)
    
    with open(output_file, 'w', encoding = 'UTF8') as file:
        df = pd.DataFrame.from_dict(data)
        file_name = input_file.split('_')
        df.insert(0, 'filing_date', file_name[2], inplace = True)
        df.insert(0, 'report_type', file_name[1], inplace = True)
        df.insert(0, 'symbol', file_name[0], inplace = True)
        df.to_csv(file)

    

#athul
import os
from collections import Counter

def write_document_sentiments(input_folder, output_file):
    # Define a dictionary to store the sentiment counts
    sentiment_counts = {
        'positive': 0,
        'negative': 0,
        'neutral': 0
    }

    # Loop through each file in the input folder
    for filename in os.listdir(input_folder):
        # Read the file
        with open(os.path.join(input_folder, filename), 'r') as f:
            text = f.read()

        # Count the number of words in the document belonging to each sentiment
        positive_count = text.count('positive_sentiment_word')
        negative_count = text.count('negative_sentiment_word')
        neutral_count = text.count('neutral_sentiment_word')

        # Add the counts to the sentiment_counts dictionary
        sentiment_counts['positive'] += positive_count
        sentiment_counts['negative'] += negative_count
        sentiment_counts['neutral'] += neutral_count