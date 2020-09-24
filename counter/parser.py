import requests
import yaml
from bs4 import BeautifulSoup
from pathlib import Path
from counter.logger import Logger


class Parser:
    logger = Logger()

    def get_tags_numbers(self, url: str):
        url = self.get_url(url)

        self.logger.info(url)

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

        return yaml.dump(results)

    def get_url(self, url: str):

        with open(str(Path(__file__).parent.absolute()) + '\\aliases.yaml', 'r') as aliases_file:
            try:
                aliases = yaml.safe_load(aliases_file)
                full_url = aliases[url]
            except yaml.YAMLError:
                full_url = url
            except KeyError:
                full_url = url

        if not full_url.lower().startswith("http"):
            full_url = "https://" + full_url

        return full_url
