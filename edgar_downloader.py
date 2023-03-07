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

    if index == '10-k':
         write_file(f,destination_folder)
    