import requests
import os
from dotenv import load_dotenv
from scraping import reading_file

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

links_sent = set()

def send_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)


def read_links_txt():
    if os.path.exists("sent.txt"):
        with open("sent.txt", "r", encoding="utf-8") as file:
            for line in file:
                links_sent.add(line.strip())
        return True
    return False


def add_link_txt(link):
    if link not in links_sent:
        with open("sent.txt", "a", encoding="utf-8") as file:
            file.write(link + "\n")
        return True
    return False


read_links_txt()
links = reading_file()

for link in links:
    if add_link_txt(link):
        send_message(link)
