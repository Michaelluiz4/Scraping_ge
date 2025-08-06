from scraping import run_scraping
from bot_telegram import send_message

def main():
    # main function
    new_links = run_scraping()
    for link in new_links:
        send_message(link)

if __name__ == "__main__":
    main()
    