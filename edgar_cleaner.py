


import requests
from bs4 import BeautifulSoup

def clean_html_text(html_text):

    soup = BeautifulSoup(html_text, 'html.parser')
    text = soup.get_text()


    import re
    clean_text = re.sub('[^A-Za-z0-9]+', ' ', text)
    print(clean_text)




def write_clean_html_text_files(input_folder, dest_folder):


    # Get a list of all the file names in the folder
    file_names = os.listdir(input_folder)


    # Loop through the file names

    for file_name in file_names:
        my_file = open(file_name,'r')

        html_text = myfile.read()

        clean_file = clean_html_text(html_text)


        file_path = os.path.join(destination_folder, file_name)

        
