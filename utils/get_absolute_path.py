import os


def get_absolute_path(path: str) -> str:
    """
    Description
    -----------
        Returns the absolute path of a file or folder

    Parameters
    -----------
        path : str
            Path to our file

    Returns
    --------
        absolute_path : str
            Our absolute path
    """

    return f'{os.getenv("DIR_TO_WATCH")}/{path}'
