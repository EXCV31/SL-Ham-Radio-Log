import platform
import subprocess


def clear_console():
    """
    Function used to clear console when user gets into any module. Support Linux/MacOS/Windows.

    Returns:
    """
    if platform.system() == "Linux" or platform.system() == "Darwin":
        subprocess.run("clear")
    else:
        subprocess.run("cls")
