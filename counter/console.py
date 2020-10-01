from counter.services.parser import Parser
from counter.services.client import Client
from counter.services.aliases.aliases import Aliases
from counter.services.storage import Storage
from counter.services.logger import Logger
import yaml


def console_view(domain_name: str):
    logger = Logger()

    with Storage() as storage:
        alias = Aliases()
        url = alias.get_url(domain_name)
        logger.info(url)

        url_on_storage = storage.find_url(url)

        if url_on_storage is not None:
            results = storage.get_tags(url)
            print('Data from db: \n===================')
        else:
            response = Client(url)
            parser = Parser(response.get_content())
            results = parser.count_tags()
            print('Data from parser: \n===================')

            if 'error' in results:
                print(yaml.dump(results))
                return

            storage.save_tags(url, results)

    print('Result: \n' + yaml.dump(results))
    pass
