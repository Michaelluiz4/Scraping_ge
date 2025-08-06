import requests
import os
from dotenv import load_dotenv
from scraping import run_scraping

load_dotenv()

TOKEN = os.getenv("TOKEN") # telegram token
CHAT_ID = os.getenv("CHAT_ID") # telegram chat id

links_sent = set()
FILE_PATH = "sent.txt"

def send_message(message):
    # send message to telegram via bot
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error" + e)


def read_links_txt():
    # read links in read.txt
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r", encoding="utf-8") as file: 
            for line in file:
                links_sent.add(line.strip())


def add_link_txt(link):
    # write in file sent.txt
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
