from counter.parser import Parser
from counter.aliases import Aliases
from counter.storage import Storage
from counter.logger import Logger
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
            print('FROMM db')
        else:
            parser = Parser(url)
            results = parser.count_tags()
            print('FROMM parser')

            if results is None:
                print('Error: Invalid URL or Connection problems')
                return

            storage.save_tags(url, results)

    print('Result:\n', yaml.dump(results))
    pass
