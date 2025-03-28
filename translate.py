import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus, unquote

# Function to get supported languages from Google Translate page
def google_get_supported_languages():
    url = "https://cloud.google.com/translate/docs/languages"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the table with the supported languages
    table = soup.find_all('table')[0]
    rows = table.find_all('tr')
    
    # Extract the languages and ISO codes into a dictionary
    languages = {}
    for row in rows[1:]:  # Skip the header row
        cols = row.find_all('td')
        if len(cols) >= 2:
            language_name = cols[0].get_text(strip=True)
            iso_code = cols[1].get_text(strip=True)
            languages[iso_code] = language_name
    
    return languages

# Function to check if a language code is valid
def google_is_valid_language_code(language_code):
    supported_languages = google_get_supported_languages()
    return language_code == "auto" or language_code in supported_languages or language_code in ["zh-CN", "zh-TW"]

# Function to split text into chunks
def split_text(text, chunk_size):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

# Function to translate long text
def google_translate_long_text(text, target_language="zh-CN", source_language="auto", chunk_size=1000):
    if not google_is_valid_language_code(target_language):
        raise ValueError("Invalid target language code.")
    
    if not google_is_valid_language_code(source_language):
        raise ValueError("Invalid source language code.")
    
    # Split the text into chunks if it's too long
    if len(text) > chunk_size:
        text_chunks = split_text(text, chunk_size)
    else:
        text_chunks = [text]
    
    translations = []
    
    # Translate each chunk
    for chunk in text_chunks:
        formatted_text = quote_plus(chunk)  # URL encode the text
        formatted_link = f"https://translate.google.com/m?tl={target_language}&sl={source_language}&q={formatted_text}"
        
        response = requests.get(formatted_link)
        
        if response.status_code == 200:
            # Parse the translated text from the response
            soup = BeautifulSoup(response.text, 'html.parser')
            translation = soup.find('div', class_='result-container').get_text(strip=True)
            translations.append(unquote(translation))  # URL decode the translation
        else:
            raise ValueError(f"Translation failed for chunk: {chunk}")
    
    # Combine translated chunks and return the result
    return " ".join(translations)

