import logging


class Logger:
    innerLogger = logging.getLogger('logger')
    innerLogger.setLevel(logging.INFO)

    file_handler = logging.FileHandler('tags_counter.log')
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s; %(message)s", "%Y-%m-%d %H:%M:%S")
    file_handler.setFormatter(formatter)

    innerLogger.addHandler(file_handler)

    def info(self, url: str):
        self.innerLogger.info(url)
