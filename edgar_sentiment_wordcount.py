import csv

def write_document_sentiments(input_folder, output_file):
    '''
    Takes a folder with cleaned html files and outputs a
    dataframe of word sentiments for each year
    '''

    data = []
    for file in input_folder:
        sentiment_data = file.get_sentiment_word_dict() # Part 3C function - Outputs dictionary of word sentiments
        data.append(sentiment_data)

    with open(output_file, 'w') as file:
        writer = csv.writer(file)
        for year in data:
            writer.writerow(year)

    file.close()

     