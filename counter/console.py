from counter.parser import Parser


def run_console(url: str):
    parser = Parser()
    result = parser.get_tags_numbers(url)

    if result is None:
        print('Error: Invalid URL or Connection problems')
        return

    print('Result:\n', result)
    pass
