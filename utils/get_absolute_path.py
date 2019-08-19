import os


def get_absolute_path(path: str):
    """
    Description:
        Gets the absoulte path of a file or folder

    Args:
        path(string): Path to our file

    Returns:
        String: The absolute path.
    """

    return f'{os.getenv("DIR_TO_WATCH")}/{path}'
