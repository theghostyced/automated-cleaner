#!/usr/bin/python3

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileModifiedEvent
from pathlib import Path
from config import DEFAULT_FOLDERS
from utils.get_absolute_path import get_absolute_path
from utils.get_current_date import get_current_date
from logger import Logger
from cleaner import Cleaner

import os
import shutil
import settings


class AutomatedMaid(FileSystemEventHandler):
    """
    Description
    -----------
        She takes care of cleaning up files added into our downloads folder.

    Attributes
    ----------
        dir_to_watch : str
            a string that holds the path to te folder we want to watch.

        destination_dir : str
            a string holding the destination folder we want our files in.
    """

    def __init__(self):
        """
        Description
        -----------
            Sets our default variable path.
        """

        self.dir_to_watch = os.getenv("DIR_TO_WATCH")
        self.destination_dir = os.getenv("DESTINATION_DIR")

        self.logger = Logger()
        self.cleaner = Cleaner()

        self.EXTENSION_TYPES = {
            'Music': ['mp3', 'wav', 'aif', 'mid'],
            'Videos': ['mp4', 'avi', '3gp', 'ogg', 'flv', 'wmv'],
            'Applications': ['app', 'dmg'],
            'Documents': ['txt', 'doc', 'pdf', 'odt', 'rtf', 'tex', 'wpd', 'docx'],
            'Archived': ['zip', 'tar', '7z', 'rar', 'gz', 'sitx', 'iso'],
            'Torrent Files': ['torrent'],
            'Images': ['jpg', 'gif', 'png', 'tiff', 'eps']
        }

    def create_default_folders(self):
        """
        Description
        -----------
            Create the defaut folders specified in the settings.py file.
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
            Create a folder in the given base_url.

        Parameters
        ----------
            filepath : str
                Path to the directory that needs to be generated.

        Returns
        -------
            None

        Raises
        ------
            OSError
                If the folder already exists.
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
                Path to the folder we wish to verify its existence.

        Returns
        -------
            folder_exists : bool
                Returns either True or False.
        """

        folder_exists = True if os.path.exists(folder_path) else False
        return folder_exists

    def move_file_to_folder(self, filename: str, dest_path: str) -> bool:
        """
        Description
        -----------
            Moves filename to the given destination path
        
        Parameters
        ----------
            file : str
                The file we wish to move to the folder
            
            dest_path : str
                The destination path that the file would be moved to
            
        Returns
        -------
            None
        """

        folder_exist = self.check_folder_existence(dest_path)

        if folder_exist:
            shutil.move(get_absolute_path(filename), dest_path)
            self.logger.write(f'Moving {filename} to the {dest_path} path')
        else:
            self.logger.write(f'Creating the {dest_path} path')
            self.generate_folder(dest_path)

            self.logger.write(f'Moving {filename} to the {dest_path} path')
            shutil.move(get_absolute_path(filename), dest_path)

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

    def determine_file_folder_location(self, extension_type: str) -> str:
        """
        Description
        -----------
            Gets the appropriate folder via the extension_type

        Parameters
        ----------
            extension_type : str
                The extension type of the file we want to move
        
        Returns
        -------
            folder_name : str
                The folder name determined by the folder location
        """

        for key, value in self.EXTENSION_TYPES.items():
            if extension_type in value:
                return key

        return 'Others'    

    def on_modified(self, event: FileModifiedEvent):
        """
        Description
        -----------
            Event is invoked whenever the directory being watched is modified.

        Parameters
        ----------
            event : FileModifiedEvent
                The event that represents file/directory modification.

        References
        ----------
            FileModifiedEvent:
                https://pythonhosted.org/watchdog/api.html#watchdog.events.FileSystemEventHandler

        Returns
        -------
            None
        """

        try:
            # Check if the modification occured in a path aside inside the `Downloads`
            # folder
            event_path = event.src_path.split('/')[4]
        except IndexError:
            # Return the downloads folder since the modification
            # didnt occur in any other folder
            event_path = event.src_path.split('/')[3]

        # Verify that the modification was not done in the
        # DEFAULT_FOLDERS
        if event_path not in DEFAULT_FOLDERS:
            self.execute_cleanup()

    def execute_cleanup(self):
        """
        Description
        -----------
            Takes care of the cleanup in the Downloads folder whenever
            a new file/folder is added to it
        """

        self.create_default_folders()

        for filename in self.cleaner.get_immediate_dir():
            if filename not in DEFAULT_FOLDERS:
                if not self.cleaner.is_hidden_file(filename):
                    if self.cleaner.is_dir(filename) and filename not in DEFAULT_FOLDERS:
                        self.move_file_to_folder(
                            filename,
                            get_absolute_path(f'Folders/{get_current_date()}')
                        )
                    else:
                        extension_type = self.get_file_extension(filename)
                        folder_location = self.determine_file_folder_location(extension_type)

                        self.move_file_to_folder(
                            filename,
                            get_absolute_path(f'{folder_location}/{get_current_date()}')
                        )

if __name__ == '__main__':

    maid = AutomatedMaid()
    logger = Logger()

    # ext = maid.get_file_extension('dan.hdna.mp3')
    # print(ext)

    observer = Observer()
    observer.schedule(maid, os.getenv("DIR_TO_WATCH"), recursive=True)
    observer.start()

    logger.write(f'Starting up the observer!!')

    try:
        pass
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
    # logger = Logger()
    # logger.write('Works', 'info')
