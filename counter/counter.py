import requests
import yaml
from bs4 import BeautifulSoup
import click
import logging
from pathlib import Path

logging.basicConfig(filename='tags_counter.log', filemode='w', level=logging.INFO)


def get_url(url):
    logging.info("Open aliases yaml")

    with open(str(Path(__file__).parent.absolute()) + '\\aliases.yaml', 'r') as aliases_file:
        try:
            logging.info("Load aliases")
            aliases = yaml.safe_load(aliases_file)
            full_url = aliases[url]
            logging.info("Found alias")
        except yaml.YAMLError:
            logging.error("Can't parse yaml")
            full_url = url
        except KeyError:
            logging.info("Can't find alias")
            full_url = url

    if not full_url.lower().startswith("http"):
        logging.info("Add https prefix to url")
        full_url = "https://" + full_url

    return full_url


def get_tags_numbers(url):
    url = get_url(url)

    try:
        logging.info("Get html page")
        response = requests.get(url)
        logging.info("Parse html page")
        soup = BeautifulSoup(response.text, "html.parser")

        results = {}
        for tag in soup.findAll():
            results[tag.name] = len(soup.findAll(tag.name))

    except requests.exceptions.InvalidURL:
        logging.error("Invalid Url")
        return None
    except requests.exceptions.ConnectionError:
        logging.error("Connection error")
        return None

    return yaml.dump(results)


def get_data(url):
    result = get_tags_numbers(url)

    if result is None:
        print('Error: Invalid URL or Connection problems')
        return

    logging.info("Show parsing result")
    print('Result:\n', result)
    pass


@click.command()
@click.option('--get', '-g', help='get list of tags')
def main(get):
    if get is not None:
        get_data(get)


if __name__ == "__main__":
    main()
