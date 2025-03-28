import time
import asyncio
import json
import os
import requests
from googletrans import Translator
from urllib.parse import quote_plus, unquote
from bs4 import BeautifulSoup
import aiohttp

# Test cases for translation
test_cases = [
    ("Hello, how are you?", "zh-CN", "auto"),
    ("I hope you're having a great day! 😊", "zh-CN", "auto"),
    ("The quick brown fox jumps over the lazy dog. This sentence contains every letter of the alphabet at least once. Python is an amazing programming language and it is highly versatile.", "zh-CN", "auto"),
    ("Computer", "zh-CN", "auto"),
    ("I love programming. Mi piace anche il caffè.", "zh-CN", "auto"),
    ("Hello, comment ça va? 今日は元気ですか?", "zh-CN", "auto"),
    ("The cost is 100 dollars for 3 items.", "zh-CN", "auto"),
    ("Quantum computing is an area of computing focused on developing computer technology based on the principles of quantum theory. Quantum algorithms and the potential power of quantum bits (qubits) make this an exciting field of study.", "zh-CN", "auto"),
    ("What time does the train leave?", "zh-CN", "auto"),
    ("The weather is nice today. I plan to go for a walk in the park later. It's a great day to enjoy the outdoors and relax.", "zh-CN", "auto"),
]

# Test translation speed using googletrans (asynchronous)
async def googletrans_translate(test_cases):
    translator = Translator()
    start_time = time.time()
    for text, target_lang, source_lang in test_cases:
        await translator.translate(text, src=source_lang, dest=target_lang)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

# Test translation speed using aiohttp and Google Translate web page
def google_translate_aiohttp(test_cases):
    async def translate_chunk_async(chunk, target_language, source_language, session):
        formatted_text = quote_plus(chunk)
        formatted_link = f"https://translate.google.com/m?tl={target_language}&sl={source_language}&q={formatted_text}"
        async with session.get(formatted_link) as response:
            if response.status == 200:
                soup = BeautifulSoup(await response.text(), 'html.parser')
                translation = soup.find('div', class_='result-container').get_text(strip=True)
                return unquote(translation)
            else:
                raise ValueError(f"Translation failed for chunk: {chunk}")

    async def google_translate_long_text_async(text, target_language="zh-CN", source_language="auto", chunk_size=1000):
        text_chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)] if len(text) > chunk_size else [text]
        async with aiohttp.ClientSession() as session:
            tasks = [translate_chunk_async(chunk, target_language, source_language, session) for chunk in text_chunks]
            translations = await asyncio.gather(*tasks)
        return " ".join(translations)

    start_time = time.time()
    asyncio.run(google_translate_long_text_async(" ".join([text for text, _, _ in test_cases]), target_language="zh-CN", source_language="auto"))
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

# Main function to compare the two methods
def compare_translation_methods():
    print("Testing googletrans method...")
    googletrans_time = asyncio.run(googletrans_translate(test_cases))
    print(f"googletrans method time: {googletrans_time:.4f} seconds\n")

    print("Testing aiohttp method...")
    aiohttp_time = google_translate_aiohttp(test_cases)
    print(f"aiohttp method time: {aiohttp_time:.4f} seconds")

if __name__ == "__main__":
    compare_translation_methods()
