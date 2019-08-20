from utils.get_absolute_path import get_absolute_path
from pathlib import Path
from typing import List

import os


class Cleaner():
    """
    Description
    -----------
        Handles our empty directory cleanup
    """

    def get_immediate_dir(self, directory: str='.') -> List[str]:
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

        return os.listdir(get_absolute_path(directory))

    def dir_cleanup(self):
        """
        Description
        -----------
            Cleans up all the empty folders present in our DEFAULT_FOLDERS
        """

        immediate_dir = self.get_immediate_dir()

        for directory in immediate_dir:
            if self.is_dir(directory):
                self.cleanup_handler(directory) if self.is_empty_dir(directory) else None

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
            Boolean: True or False
        """

        try:
            os.rmdir(Path(get_absolute_path(directory)))
            return True
        except OSError as error:
            print("Folder isn't empty")
            print(error)
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

        # Check if the length of os.listdir is 0.
        # PS - os.listdir returns an array
        # References -https://docs.python.org/2/library/os.html?highlight=os%20listdir#os.listdir
        return len(os.listdir(get_absolute_path(directory))) == 0

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

        return os.path.isdir(get_absolute_path(directory))

# REQUIREMENTS
# 1. Get the immediate folder dir.
# 2. Check each folder if it is empty
# 3. Remove those who are empty and keep those that aren't
# 4. Log the deleted folders.
