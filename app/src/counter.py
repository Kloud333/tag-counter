import requests
from bs4 import BeautifulSoup


def get_tags_numbers(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    results = {}
    for tag in soup.findAll():
        results[tag.name] = len(soup.findAll(tag.name))
    return results


tags_and_numbers = get_tags_numbers('https://www.google.com/')

print(tags_and_numbers)
