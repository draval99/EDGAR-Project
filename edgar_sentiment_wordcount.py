
import pandas as pd

def write_document_sentiments(input_folder : str, output_file : str):
    '''
    Takes a folder with cleaned html files and outputs a
    dataframe of word sentiments for each year
    '''

   # List of filenames from the input folder
    import os
    file_names = os.listdir(input_folder)

    # Define a dictionary to store the sentiment counts
    data=[]
    filenames = []
    # Loop through each file in the input folder
    for filename in os.listdir(input_folder):
        # Create a dictionary for each file, counting how many different sentiment words are present in that document
        sentiment_counts = {
        'positive': 0,
        'negative': 0,
        'neutral': 0
        }
        # Read the file
        filenames.append(filename)
        with open(os.path.join(input_folder, filename), 'r') as f:
            text = f.read()

        # Count the number of words in the document belonging to each sentiment
        positive_count = text.count('Positive')
        for word in text.split():
            if word in sentiment_dict


        negative_count = text.count('negative_sentiment_word')
        neutral_count = text.count('neutral_sentiment_word')

        # Add the counts to the sentiment_counts dictionary
        sentiment_counts['positive'] += positive_count
        sentiment_counts['negative'] += negative_count
        sentiment_counts['neutral'] += neutral_count

        # Add the dictionary to the list 'data' to get a list of dictionaries, to make an output dataframe
        data.append(sentiment_counts)
    
    with open(output_file, 'w', encoding = 'UTF8') as file:
        df = pd.DataFrame.from_dict(data)
        file_name = input_file.split('_')
        df.insert(0, 'filing_date', file_name[2], inplace = True)
        df.insert(0, 'report_type', file_name[1], inplace = True)
        df.insert(0, 'symbol', file_name[0], inplace = True)
        df.to_csv(file)
