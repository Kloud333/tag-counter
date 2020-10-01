from bs4 import BeautifulSoup


class Parser:
    def __init__(self, response):
        self.response = response

    def count_tags(self):
        try:
            soup = BeautifulSoup(self.response, "html.parser")

            results = {}
            for tag in soup.findAll():
                results[tag.name] = len(soup.findAll(tag.name))

            return results if results else {'error': 'No tags found'}
        except TypeError:
            return self.response
