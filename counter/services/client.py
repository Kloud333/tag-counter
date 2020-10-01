import requests


class Client:
    def __init__(self, url):
        self.url = url

    def get_content(self):
        try:
            return requests.get(self.url).text

        except (requests.exceptions.InvalidURL, requests.exceptions.MissingSchema):
            return {'error': 'Invalid URL'}
            # raise SystemExit('Invalid URL')

        except requests.exceptions.ConnectionError:
            return {'error': 'Connection problems'}
            # raise SystemExit('Connection problems')
