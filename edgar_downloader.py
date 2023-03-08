import requests

#Athul

def write_page(url, file_path):
    # Make a GET request to the URL
    response = requests.get(url, headers = {'User-Agent' : 'williamrenouf@kubrickgroup.com'})
    
    # Check if the response was successful
    if response.status_code == 200:
        # Write the HTML content to the file
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(response.text)
            f.close()
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
    import os

    # Get a list of all the file names in the folder
    file_names = os.listdir(destination_folder)

    # Loop through the file names and delete each file
    for file_name in file_names:
        file_path = os.path.join(destination_folder, file_name)
        os.remove(file_path)


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

    url_list = []
    for i,num in enumerate(primary_document_list):
        ten_k_url = 'https://www.sec.gov/Archives/edgar/data/' + get_CIK_number(ticker, False) + '/' + accession_number_list[i] + '/' + num
        url_list.append(ten_k_url)
        filepath = destination_folder + f'\{num}'
        write_page(ten_k_url, filepath)

    
    

download_files_10k('AAPL', R'C:\Users\William Renouf\OneDrive - Kubrick Group\Documents\Python\edgar_project\test_folder')

