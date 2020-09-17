import requests
import yaml
from bs4 import BeautifulSoup


def get_url(url):
    with open("app/assets/aliases.yaml", 'r') as aliases_file:
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


def get_tags_numbers(url):
    url = get_url(url)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    results = {}
    for tag in soup.findAll():
        results[tag.name] = len(soup.findAll(tag.name))
    return results


tags_and_numbers = get_tags_numbers('ggl')

print(tags_and_numbers)
