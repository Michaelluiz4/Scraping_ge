import os
import requests
from bs4 import BeautifulSoup
import json

url = "https://ge.globo.com/futebol/times/palmeiras/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

subjects = soup.find_all("a", class_="feed-post-link")

links = set()

def reading_file():
    if os.path.exists("links.json"):
        try:
            with open("links.json", "r", encoding="utf-8") as file:
                data = json.load(file)
                return set(data)
        except json.JSONDecodeError:
            pass
    return set()


def add_subjects(existing_links):
    for subject in subjects:
        href = subject.get("href")
        if href:
            existing_links.add(href)
    return existing_links


def write_in_file(final_links):
    with open("links.json", "w", encoding="utf-8") as file:
        json.dump(list(final_links), file, ensure_ascii=False, indent=4)


stored_links = reading_file()
update_links = add_subjects(stored_links)
write_in_file(update_links)
