import requests

from bs4 import BeautifulSoup

def set_byn(usd_raw: int):
    data = requests.get("https://myfin.by/currency/usd")
    soup = BeautifulSoup(data.content, 'html.parser')
    usd = soup.find("span", {"class": "accent"}).find_next().get_text()
    result = int(usd_raw) * float(usd)
    return int(result)
