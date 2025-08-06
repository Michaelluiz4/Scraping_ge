import os
import requests
from bs4 import BeautifulSoup
import json

FILE_PATH = "links.json"

def run_scraping():
    url = "https://ge.globo.com/futebol/times/palmeiras/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    subjects = soup.find_all("a", class_="feed-post-link")

    def reading_file():
        # read file links.json if it already exists
        if os.path.exists(FILE_PATH):
            try:
                with open(FILE_PATH, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    return set(data)
            except json.JSONDecodeError:
                pass
        return set()


    def extract_new_links(existing_links):
        new_links = set()

        for subject in subjects:
            href = subject.get("href")
            if href and href not in existing_links:
                new_links.add(href)
        return new_links


    def write_in_file(final_links):
        # function to write to the file
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(list(final_links), file, ensure_ascii=False, indent=4)


    stored_links = reading_file()
    fresh_links = extract_new_links(stored_links)
    all_links = stored_links.union(fresh_links)
    write_in_file(all_links)

    return list(fresh_links)
