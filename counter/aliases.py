from pathlib import Path
import yaml


class Aliases:
    @staticmethod
    def get_url(url: str):
        with open(str(Path(__file__).parent.absolute()) + '\\aliases.yaml', 'r') as aliases_file:
            try:
                aliases = yaml.safe_load(aliases_file)
                full_url = url if '.' in url else aliases[url]
            except yaml.YAMLError:
                full_url = url
            except KeyError:
                full_url = url

            if not full_url.lower().startswith("http"):
                full_url = "https://" + full_url

        return full_url
