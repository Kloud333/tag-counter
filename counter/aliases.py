from pathlib import Path
import yaml
from counter.logger import Logger


class Aliases:
    logger = Logger()

    def __init__(self):
        self.path = str(Path(__file__).parent.absolute()) + '\\aliases.yaml'
        if self.path is not None:
            self.read(self.load_yaml)

    def get_url(self, url: str):
        full_url = url if '.' in url else self.aliases[url]

        if not full_url.lower().startswith("http"):
            full_url = "https://" + full_url

        return full_url

    def show_aliases(self):
        print('Alias list:\n', yaml.dump(self.aliases))

    def remove_alias(self, alias):
        del self.aliases[alias]
        self.write(self.save)

    def add_alias(self, alias, url):
        self.aliases[alias] = url
        self.write(self.save)

    def save(self, stream):
        yaml.dump(self.aliases, stream)

    def file(self, action, mode):
        with open(self.path, mode) as stream:
            try:
                action(stream)
            except yaml.YAMLError as exc:
                self.logger.error(exc)

    def load_yaml(self, stream):
        self.aliases = yaml.safe_load(stream)

    def read(self, action):
        self.file(action, 'r')

    def write(self, action):
        self.file(action, 'w')
