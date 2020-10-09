from counter.services.aliases.aliases import Aliases
from counter.services.logger import Logger
from counter.services.parser import Parser
from counter.services.client import Client
from counter.services.storage import Storage
import yaml


class Console:
    aliases = Aliases()
    logger = Logger()

    def __init__(self, domain_name):
        self.url = self.aliases.get_url(domain_name)
        self.logger.info(self.url)

    def console_view(self):
        with Storage() as storage:
            response = Client(self.url)
            parser = Parser(response.get_content())
            results = parser.count_tags()
            print('Data from parser: \n===================')

            if 'error' in results:
                print(yaml.dump(results))
                return

            storage.save_tags(self.url, results)

        print('Result: \n' + yaml.dump(results))
        pass

    def console_view_db(self):
        with Storage() as storage:
            data = storage.get_tags(self.url)
            results = data if data else 'No Data founded'
            print('Data from db: \n===================')

        print('Result: \n' + yaml.dump(results))
        pass
