import requests

#Athul
import requests

def write_page(url, file_path):
    # Make a GET request to the URL
    response = requests.get(url)
    
    # Check if the response was successful
    if response.status_code == 200:
        # Write the HTML content to the file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(response.text)
        print(f"HTML file written to {file_path}")
    else:
        print("Failed to write HTML file")


#Will

def download_files_10k(ticker : str, destination_folder : str):
    '''
    Downloads the all the 10-k files for the given ticker and puts them into
    the destination folder path.
    '''
    def get_CIK_number(ticker : str):

        url = r'https://www.sec.gov/files/company_tickers.json'
        r = requests.get(url)
        response = r.json()
        company_info = response.values()
        for company in company_info:
            if company['ticker'] == ticker:
                output = company['cik_str']
        if len(str(output)) < 10:
            padded_output = str(output).rjust(10, '0')
            return padded_output
        else:
            return output
    
    submissions_url = 'https://data.sec.gov/submissions/CIK' + get_CIK_number(ticker) + '.json'
    print(submissions_url)

    #for url in url_list:
        #if index == '10-k':
            #write_file(url, destination_folder)
    

download_files_10k('AAPL', 1)

response['filings']['recents']['accessionNumber'] #list of accession number eg "0001104659-23-028445"
response['filings']['recents']['filingDate'] #list of filing dates eg "2023-03-03"
response['filings']['recents']['primaryDocDescription'] #list of all the pdescriptions
response['filings']['recents']['primaryDocDescription']['10-K'] # index of 10-k
