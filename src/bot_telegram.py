import requests
import os
from dotenv import load_dotenv
from scraping import run_scraping

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

links_sent = set()
FILE_PATH = "sent.txt"

def send_message(message):
    # function sent message for telegram
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error" + e)


def read_links_txt():
    # function read links in file sent.txt
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            for line in file:
                links_sent.add(line.strip())


def add_link_txt(link):
    # function add link in file sent.txt
    if link not in links_sent:
        with open(FILE_PATH, "a", encoding="utf-8") as file:
            file.write(link + "\n")
        return True
    return False


read_links_txt()
links = run_scraping()

for link in links:
    if add_link_txt(link):
        send_message(link)
