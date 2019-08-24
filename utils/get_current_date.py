from datetime import date

def get_current_date():
    """
    Description
    -----------
        Returns the current date in human readable form
    """

    return date.today().strftime("%B %d, %Y")