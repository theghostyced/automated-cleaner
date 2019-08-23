from utils.get_absolute_path import get_absolute_path
from pathlib import Path
from typing import List
from logger import Logger

import os


class Cleaner():
    """
    Description
    -----------
        Handles our empty directory cleanup
    """

    def __init__(self):
        """
        Descritpion
        -----------
            Initializes our cleaner class
        """

        self.logger = Logger()
        self.logger.write(f'Initialising the cleaner')

    def get_immediate_dir(self, directory: str = '.') -> List[str]:
        """
        Description
        -----------
            Gets all the immediate directories of the base path

        Parameters
        -----------
            directory : string
                Directory we want to look into, if none is passed the current directory is then used

        Returns
        -------
            immediate_directories : List[str]
                Returns an array of all directories
        """

        self.logger.write(
            f'Checking the immediate directories of the {directory} folder')
        return os.listdir(get_absolute_path(directory))

    def cleanup(self, directory: str):
        """
        Description
        -----------
            Cleans up all the empty folders present in our DEFAULT_FOLDERS

        Parameters
        ----------
            directory : str
                The directory we would love to clean up
        """

        immediate_dir = self.get_immediate_dir(directory)

        for folder in immediate_dir:
            if self.is_dir(folder):
                self.cleanup_handler(folder) if self.is_empty_dir(
                    folder) else None

    def cleanup_handler(self, directory: str) -> bool:
        """
        Description
        -----------
            Cleans up empty directories

        Parameters
        -----------
            directory : string
                Directory to clean up

        Returns
        -------
            bool
        """

        try:
            self.logger.write(f'Deleting the {directory} folder')
            os.rmdir(Path(get_absolute_path(directory)))
            return True
        except OSError as error:
            print("Folder isn't empty")
            print(error)
            self.logger.write(
                f'Could not delete the {directory} folder. {error} thrown',
                'exception')
            return False

    def is_empty_dir(self, directory: str) -> bool:
        """
        Description
        -----------
            Checks if the folder is empty

        Parameters
        ----------
            directory : string
                Directory to verify

        Returns
        -------
            bool
        """

        self.logger.write(f'Checking if the {directory} is empty')

        # Check if the length of os.listdir is 0.
        # PS - os.listdir returns an array
        # References -https://docs.python.org/2/library/os.html?highlight=os%20listdir#os.listdir
        return len(os.listdir(get_absolute_path(directory))) == 0
    
    def is_hidden_file(self, directory: str) -> bool:
        """
        Descritpion
        -----------
            Determines if the file sent is a hidden file or not
        
        Parameters
        ----------
            directory : str
                Directory we wish to verify
        
        Returns
        -------
            bool
        """

        return False if directory[:1] != '.' else True

    def is_dir(self, directory: str) -> bool:
        """
        Description
        -----------
            Checks if the path is a directory

        Parameters
        ----------
            directory : string
                The directory name

        Returns
        -------
            bool
        """

        self.logger.write(
            f'Checking if the given path {directory} is a valid directory')
        return os.path.isdir(get_absolute_path(directory))
