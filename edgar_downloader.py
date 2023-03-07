import requests

#Athul
import requests

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