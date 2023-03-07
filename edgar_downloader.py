import requests

#Athul

def write_page(url, file_path):
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(file_path, 'w') as f:
            f.write(response)
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
    def get_CIK_number(ticker : str):
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
                output = company['cik_str']
        if len(str(output)) < 10:
            padded_output = str(output).rjust(10, '0')
            return padded_output
        else:
            return output
    
    submissions_url = 'https://data.sec.gov/submissions/CIK' + get_CIK_number(ticker) + '.json'
    file = requests.get(submissions_url)
    response = file.json()
    ten_k_index_positions = []
    print(response)



    
    

download_files_10k('AAPL', 1)