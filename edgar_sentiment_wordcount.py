import csv
import pandas as pd

def write_document_sentiments(input_folder, output_file):
    '''
    Takes a folder with cleaned html files and outputs a
    dataframe of word sentiments for each year
    '''

    data = []
    for file in input_folder:
        sentiment_data = file.get_sentiment_word_dict() # Part 3C function - Outputs dictionary of word sentiments
        data.append(sentiment_data)
    
    with open(output_file, 'w', encoding = 'UTF8', newline = '') as file:
        df = pd.DataFrame.from_dict(data)
        file_name = output_file.split('_')
        df.insert(0, 'filing_date', file_name[2], inplace = True)
        df.insert(0, 'report_type', file_name[1], inplace = True)
        df.insert(0, 'symbol', file_name[0], inplace = True)

    

     