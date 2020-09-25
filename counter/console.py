from counter.parser import Parser
from counter.aliases import Aliases
from counter.storage import Storage


def run_console_view(domain_name: str):
    with Storage() as storage:
        url = Aliases.get_url(domain_name)
        parser = Parser(url, aliases=Aliases, storage=storage)
        result = parser.count_tags()

    if result is None:
        print('Error: Invalid URL or Connection problems')
        return

    print('Result:\n', result)
    pass
