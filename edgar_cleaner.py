


import requests
from bs4 import BeautifulSoup
import re
import os
import edgar_downloader




def clean_html_text(html_text):

    soup = BeautifulSoup(html_text, 'html.parser')
    text = soup.get_text()


    clean_text = re.sub('[^A-Za-z0-9]+', ' ', text)
    print(clean_text)




def write_clean_html_text_files(input_folder, dest_folder):


    # Get a list of all the file names in the folder
    file_names = os.listdir(input_folder)


    # Loop through the file names

    for file_name in file_names:
        
        my_file = open(file_name,'r')

        html_text = my_file.read()

        clean_file = clean_html_text(html_text)

        #<ticker>_10-k_<filing_date>.txt.

        new_file_name = file_name.remove('html') 
        
        file_name = new_file_name + '.txt'

        file_path = os.path.join(dest_folder, file_name)






        

        
