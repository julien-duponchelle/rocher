import os

def path() -> str:
    """
    Returns the absolute path to the installation of the Monaco editor.
    """
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "vs")
