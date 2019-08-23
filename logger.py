from pathlib import Path

import logging
import datetime


class Logger:
    """
    Description
    -----------
        Controls logging of our messages into a file

    Attributes
    ----------
        LOGGING_FORMAT : str
            a string format signifying our logging format

        DEFAULT_LOGGING_LEVEL : logging.DEBUG
            indicates our default logging level
                https://docs.python.org/3/library/logging.html#logging-levels
    """

    def __init__(self):
        """
        Description
        -----------
            Initializer for our class
        """

        LOGGING_FORMAT = '%(levelname)s - %(asctime)s - %(name)s - %(module)s - %(message)s'
        DEFAULT_LOGGING_LEVEL = logging.DEBUG

        # Path to our log file
        self.log_filename = Path('.') / 'logs' / 'am_log.log'

        logging.basicConfig(format=LOGGING_FORMAT,
                            level=DEFAULT_LOGGING_LEVEL,
                            filename=self.log_filename)

        logger = logging.getLogger()

        # Setting out logging levels so it can be called
        # based on the type a user passes in the write fn
        self.LOGGING_LEVELS = {
            'info': logger.info,
            'error': logger.error,
            'warning': logger.warning,
            'exception': logger.exception
        }

    def write(self, msg: str, type: str = 'info'):
        """
        Description
        -----------
            Takes care of writing to our text file

        Parameters
        ----------
            msg : str
                The message we wish to log in our file
            type : str
                The type of logging level we wish to use

        Returns
        -------
            None
        """
        try:
            print(msg)
            self.LOGGING_LEVELS[type](msg)
        except:
            raise ('Invalid logging level provided!')
