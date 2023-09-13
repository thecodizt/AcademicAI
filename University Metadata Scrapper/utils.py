import requests
from bs4 import BeautifulSoup
from langdetect import detect

def isUrlValid(url):
    try:
        response = requests.get(url)
        # If the request was successful, the status code will be 200
        return response.status_code == 200
    except:
        return False

def isContentEnglish(url):
    try:
        response = requests.get(url, timeout=1)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        # Detect the language of the text
        language = detect(text)
        # Check if the language is English
        return language == 'en'
    except:
        return False