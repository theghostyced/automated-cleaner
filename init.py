from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
from config import DEFAULT_FOLDERS

import os
import time
import settings


class AutomatedMaid(FileSystemEventHandler):
    """
    Description:
        She takes care of cleaning up files added into our downloads folder
    """

    def __init__(self):
        """
        Description:
            Sets our default variable path.
        """

        self.dir_to_watch = os.getenv("DIR_TO_WATCH")
        self.destination_dir = os.getenv("DESTINATION_DIR")

    def create_default_folders(self):
        """
        Description:
            Create the defaut folders specified in the settings.py file
        """

        for folder_name in DEFAULT_FOLDERS:
            dir_path = f'{self.destination_dir}/{folder_name}'

            folder_exists = self.check_folder_existence(dir_path)

            if not folder_exists:
                os.mkdir(Path(dir_path))

    def generate_folder(self, filepath):
        """
        Description:
            Create a folder in the given base_url

        Args:
            filepath(string): Path to the directory that needs to be
            generated

        Returns:
            None

        """

        try:
            return os.mkdir(filepath)
        except OSError as error:
            print('Folder already exists!')
            print(error)

    def check_folder_existence(self, folder_path):
        """
        Description:
            Checks for the existence of a folder in our parent dir.

        Args:
            folder_path(string): Path to the folder we wish to verify its
            existence

        Returns:
            Boolean - Returns either True or False
        """

        folder_exists = True if os.path.exists(folder_path) else False
        return folder_exists

    def get_absolute_path(self, path):
        """
        Description:
            Gets the absoulte path of a file or folder

        Args:
            path(string): Path to our file

        Returns:
            String: The absolute path.
        """

        return f'{self.dir_to_watch}/{path}'

    def dir_cleanup(self):
        """
        Description:
            Cleans up all the empty folders present in our DEFAULT_FOLDERS
        """

        immediate_dir = self.get_immediate_dir()

        for directory in immediate_dir:
            if self.is_dir(directory):
                pass

    def cleanup_handler(self, directory):
        """
        Description:
            Cleans up empty directories
        """

        return os.rmdir(Path(self.get_absolute_path(directory)))

    def is_empty_dir(self, directory):
        """
        Description:
            Checks if the folder is empty
        """

        # Check if the length of os.listdir is 0.
        # PS - os.listdir returns an array
        # References -https://docs.python.org/2/library/os.html?highlight=os%20listdir#os.listdir
        return len(os.listdir(self.get_absolute_path(directory))) == 0

    def is_dir(self, directory):
        """
        Description:
            Checks if the path is a directory

        Args:
            directory(string): The directory name

        Returns:
            Boolean - True or False
        """

        return os.path.isdir(self.get_absolute_path(directory))

    def get_immediate_dir(self, directory='.'):
        """
        Description:
            Gets all the immediate directories of the base path

        Args:
            directory(string): Directory we want to look into, if none is passed
            the current directory is then used

        Returns:
            Array: Returns an array of all directories
        """

        return os.listdir(self.get_absolute_path(directory))

    def get_file_extension(self, filename):
        """
        Description:
            Gets the given extension for a file

        Args:
            filename(string): The file's name

        Returns:
            extension_type: The file extension type given
        """

        # Returns the last item in the array incase of muliple dot operator.
        return filename.split('.')[-1]

    def on_modified(self, event):
        """
        Description:
            Event is invoked whenever the directory being watched is modified.

        Args:
            event(FileModifiedEvent): The event that represents file/directory
            modification

        References:
            FileModifiedEvent:
                https://pythonhosted.org/watchdog/api.html#watchdog.events.FileSystemEventHandler

        Returns:
            None
        """
        return super().on_modified(event)


if __name__ == '__main__':

    maid = AutomatedMaid()
    ext = maid.get_file_extension('dan.hdna.mp3')
    print(ext)
    print(maid.is_empty_dir('.'))
