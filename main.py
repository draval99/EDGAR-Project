from edgar_downloader import download_files_10k
from edgar_cleaner import write_clean_html_text_files

from edgar_sentiment_wordcount import write_document_sentiments

download_files_10k('AAPL', R'C:\Users\William Renouf\OneDrive - Kubrick Group\Documents\Python\edgar_project\test_folder_raw')
write_clean_html_text_files(R'C:\Users\William Renouf\OneDrive - Kubrick Group\Documents\Python\edgar_project\test_folder_raw', R'C:\Users\William Renouf\OneDrive - Kubrick Group\Documents\Python\edgar_project\test_folder_clean')

write_document_sentiments(R'C:\Users\William Renouf\OneDrive - Kubrick Group\Documents\Python\edgar_project\test_folder_clean', R'C:\Users\William Renouf\OneDrive - Kubrick Group\Documents\Python\edgar_project\test_folder_csv')