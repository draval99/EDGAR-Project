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
