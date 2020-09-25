import logging


class Logger:
    innerLogger = logging.getLogger('logger')
    innerLogger.setLevel(logging.INFO)

    file_handler = logging.FileHandler('tags_counter.log')
    file_handler.setLevel(logging.INFO)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.ERROR)

    formatter = logging.Formatter("%(asctime)s; %(message)s", "%Y-%m-%d %H:%M:%S")
    file_handler.setFormatter(formatter)

    innerLogger.addHandler(file_handler)
    innerLogger.addHandler(stream_handler)

    def info(self, message: str):
        self.innerLogger.info(message)

    def error(self, message: str):
        self.innerLogger.error(message)
