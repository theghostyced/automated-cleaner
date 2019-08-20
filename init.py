from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileModifiedEvent
from pathlib import Path
from config import DEFAULT_FOLDERS
from utils.get_absolute_path import get_absolute_path

import os
import time
import settings
from logger import Logger


class AutomatedMaid(FileSystemEventHandler):
    """
    Description
    -----------
        She takes care of cleaning up files added into our downloads folder

    Attributes
    ----------
        dir_to_watch : str
            a string that holds the path to te folder we want to watch

        destination_dir : str
            a string holding the destination folder we want our files in
    """

    def __init__(self):
        """
        Description
        -----------
            Sets our default variable path.
        """

        self.dir_to_watch = os.getenv("DIR_TO_WATCH")
        self.destination_dir = os.getenv("DESTINATION_DIR")

    def create_default_folders(self):
        """
        Description
        -----------
            Create the defaut folders specified in the settings.py file
        """

        for folder_name in DEFAULT_FOLDERS:
            dir_path = f'{self.destination_dir}/{folder_name}'

            folder_exists = self.check_folder_existence(dir_path)

            if not folder_exists:
                os.mkdir(Path(dir_path))

    def generate_folder(self, filepath: str):
        """
        Description
        -----------
            Create a folder in the given base_url

        Parameters
        ----------
            filepath : str
                Path to the directory that needs to be generated

        Returns
        -------
            None

        Raises
        ------
            OSError
                If the folder already exists
        """

        try:
            return os.mkdir(filepath)
        except OSError as error:
            print('Folder already exists!')
            print(error)

    def check_folder_existence(self, folder_path: str) -> bool:
        """
        Description
        -----------
            Checks for the existence of a folder in our parent dir.

        Parameters
        ----------
            folder_path : str
                Path to the folder we wish to verify its existence

        Returns
        -------
            folder_exists : bool
                Returns either True or False
        """

        folder_exists = True if os.path.exists(folder_path) else False
        return folder_exists

    def get_file_extension(self, filename: str) -> str:
        """
        Description
        -----------
            Gets the given extension for a file

        Parameters
        ----------
            filename : str
                The file's name

        Returns
        -------
            extension_type : str
                The file extension type given
        """

        # Returns the last item in the array incase of muliple dot operator.
        return filename.split('.')[-1]

    def on_modified(self, event: FileModifiedEvent):
        """
        Description
        -----------
            Event is invoked whenever the directory being watched is modified.

        Parameters
        ----------
            event : FileModifiedEvent
                The event that represents file/directory modification

        References
        ----------
            FileModifiedEvent:
                https://pythonhosted.org/watchdog/api.html#watchdog.events.FileSystemEventHandler

        Returns
        -------
            None
        """

        print('Modified', event.src_path)


if __name__ == '__main__':

    maid = AutomatedMaid()
    # ext = maid.get_file_extension('dan.hdna.mp3')
    # print(ext)

    # observer = Observer()
    # observer.schedule(maid, os.getenv("DIR_TO_WATCH"), recursive=True)
    # observer.start()

    # try:
    #     pass
    # except KeyboardInterrupt:
    #     observer.stop()

    # observer.join()
    logger = Logger()
    logger.write('Works', 'info')
