from counter.parser import Parser
from counter.aliases import Aliases
from counter.storage import Storage
from counter.logger import Logger


def console_view(domain_name: str):
    logger = Logger()

    with Storage() as storage:
        alias = Aliases()
        url = alias.get_url(domain_name)
        logger.info(url)

        parser = Parser(url)
        results = parser.count_tags()

        storage.save_tags(url, results)

    if results is None:
        print('Error: Invalid URL or Connection problems')
        return

    print('Result:\n', results)
    pass
