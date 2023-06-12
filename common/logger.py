import logging


class Logger:
    def __init__(self) -> None:
        self._logger = logging.getLogger('testarena')
        self.debug = self._logger.debug
        self.info = self._logger.info
        self.warning = self._logger.warning
        self.error = self._logger.error
        self.critical = self._logger.critical
