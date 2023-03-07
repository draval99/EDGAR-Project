import requests

#Athul

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

    1st Arguement - Company ticker - Required to be string

    2nd Arguement - Folder to write 10-k HTML files to 
                    Note: Does not need the root file path

    '''
    def get_CIK_number(ticker : str, padded = True):
        '''
        
        Fucntion to obtain the CIK identifier for a given company ticker.

        Fucntion Arguements:
            1st Arguement - Company ticker - Required to be string

        '''

        url = r'https://www.sec.gov/files/company_tickers.json'
        r = requests.get(url)
        response = r.json()
        company_info = response.values()
        for company in company_info:
            if company['ticker'] == ticker:
                output = str(company['cik_str'])
        if padded == True:
            if len(str(output)) < 10:
                padded_output = output.rjust(10, '0')
                return padded_output
            else:
                return output
        else:
            return output
    
    cik_number = get_CIK_number(ticker)
    
    submissions_url = 'https://data.sec.gov/submissions/CIK' + cik_number + '.json'
    r = requests.get(submissions_url, headers = {'User-Agent' : 'williamrenouf@kubrickgroup.com'})
    response = r.json()
    
    form_type_list = response['filings']['recent']['primaryDocDescription']
    index_positions = [i for i,form in enumerate(form_type_list) if form == '10-K']

    accession_number_list = []
    primary_document_list = []
    for i in index_positions:
        num = response['filings']['recent']['accessionNumber'][i]
        new_num = num.replace('-', '')
        accession_number_list.append(new_num)
        url_str = response['filings']['recent']['primaryDocument'][i]
        primary_document_list.append(url_str)

    
    ten_k_url = 'https://www.sec.gov/Archives/edgar/data/' + get_CIK_number(ticker, False) + '/' + accession_number_list[0] + '/' + primary_document_list[0]
    print(ten_k_url)
    





    
    

download_files_10k('AAPL', 1)

#response['filings']['recents']['accessionNumber'] #list of accession number eg "0001104659-23-028445"
#response['filings']['recents']['filingDate'] #list of filing dates eg "2023-03-03"
#response['filings']['recents']['primaryDocDescription'] #list of all the pdescriptions
#response['filings']['recents']['primaryDocDescription']['10-K'] # index of 10-k
#headers = {'User-Agent' : 'williamrenouf@kubrickgroup.com'}
