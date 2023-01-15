import logging
from rich.panel import Panel
from rich.text import Text
from rich.console import Console
import platform
import subprocess
import time

# File imports
from helpers.colors import get_color
from config.setup_config import radio_conf, frame_title

logging.basicConfig(filename='SL_Ham_Radio_Log.log', encoding='utf-8', level=logging.DEBUG, format='[%(asctime)s] %('
                                                                                                   'levelname)s: %('
                                                                                                   'message)s')

console = Console()


def welcome():
    """
    Log into redmine and greet user. Also, here we have error handler, for auth, connection and permission errors.

    Returns:

    """
    console.rule(
        f"[{get_color('bold_orange')}]SL Ham Radio Log [{get_color('white')}]-"
        f" [{get_color('blue')}]Trwa ładowanie aplikacji...", )

    # Clear terminal
    if platform.system() == "Linux" or platform.system() == "Darwin":
        subprocess.run("clear")
    else:
        subprocess.run("cls")

    logging.info(f"Połączenie zakończone sukcesem. Zalogowany jako {radio_conf['OPERATOR']} - {radio_conf['CALLSIGN']}")

    console.print(Panel(Text("\nZalogowano pomyślnie!\n"
                             f"\nUżytkownik: {radio_conf['OPERATOR']}"
                             f"\nZnak wywoławczy: {radio_conf['CALLSIGN']}\n", justify="center", style="white"),
                        style=get_color("green"), title=frame_title))

    # It just better look with that.
    time.sleep(0.5)
