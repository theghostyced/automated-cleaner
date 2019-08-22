from cleaner import Cleaner
from config import DEFAULT_FOLDERS
from logger import Logger


def empty_dir_cleanup_job():
    """
    Description
    -----------
        Job to clean up all our empty dir.
    """

    cleaner = Cleaner()
    logger = Logger()

    for folder in DEFAULT_FOLDERS:
        cleaner.cleanup(folder)
        logger.write(f'Cleaning up empty dir in the {folder} folder')
