from edgar_downloader import download_files_10k
from edgar_cleaner import write_clean_html_text_files

download_files_10k('AAPL', R'C:\Users\William Renouf\OneDrive - Kubrick Group\Documents\Python\edgar_project\test_folder_raw')
write_clean_html_text_files(R'C:\Users\William Renouf\OneDrive - Kubrick Group\Documents\Python\edgar_project\test_folder_raw', R'C:\Users\William Renouf\OneDrive - Kubrick Group\Documents\Python\edgar_project\test_folder_clean')