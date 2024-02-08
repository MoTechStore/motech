import requests
from bs4 import BeautifulSoup
import os
import urllib.request



def get_file_names(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        file_names = []
        for link in soup.find_all('a'):
            href = link.get('href')
            # Filter out parent directory links and URLs with fragments
            if href and href != '../' and not href.startswith('#'):
                file_names.append(href)
        return file_names
    else:
        print("Failed to fetch URL:", url)
        return []

# Example usage:
url = "https://pmis.posta.co.tz/assets/images/users/"
file_names = get_file_names(url)
for file_name in file_names:
    save_path = 'D:/DATASET/'+str(file_name)
    print(save_path)
    download_url = url+file_name
    #print(download_url)
    try:
        response = requests.get(download_url)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
    except Exception as e:
        print(f"Error downloading file: {e}")