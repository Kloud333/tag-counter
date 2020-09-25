import requests
import yaml
from counter.logger import Logger
from bs4 import BeautifulSoup


class Parser:
    logger = Logger()

    def __init__(self, url, aliases, storage):
        self.url = url
        self.aliases = aliases
        self.storage = storage

    def count_tags(self):
        url = self.aliases.get_url(self.url)

        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            results = {}
            for tag in soup.findAll():
                results[tag.name] = len(soup.findAll(tag.name))

        except requests.exceptions.InvalidURL:
            return None
        except requests.exceptions.ConnectionError:
            return None

        self.logger.info(url)
        self.storage.save_tags(url, results)

        return yaml.dump(results)
