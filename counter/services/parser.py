from bs4 import BeautifulSoup


class Parser:
    def __init__(self, response):
        self.response = response

    def count_tags(self):
        soup = BeautifulSoup(self.response.text, "html.parser")

        results = {}
        for tag in soup.findAll():
            results[tag.name] = len(soup.findAll(tag.name))

        if not results:
            raise SystemExit('No tags found')

        return results
