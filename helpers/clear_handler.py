import platform
import subprocess

def clear_console():
    if platform.system() == "Linux" or platform.system() == "Darwin":
        subprocess.run("clear")
    else:
        subprocess.run("cls")