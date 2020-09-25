import requests
from bs4 import BeautifulSoup
import yaml


class Parser:
    def __init__(self, url):
        self.url = url

    def count_tags(self):
        try:
            response = requests.get(self.url)
            soup = BeautifulSoup(response.text, "html.parser")

            results = {}
            for tag in soup.findAll():
                results[tag.name] = len(soup.findAll(tag.name))

        except requests.exceptions.InvalidURL:
            return None
        except requests.exceptions.ConnectionError:
            return None

        return results
