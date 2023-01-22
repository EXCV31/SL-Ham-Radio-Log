import logging
from rich.panel import Panel
from rich.text import Text
from rich.console import Console
import time

# File imports
from helpers.colors import get_color
from helpers.clear_handler import clear_console
from config.setup_config import radio_conf, frame_title

logging.basicConfig(filename='SL_Ham_Radio_Log.log', encoding='utf-8', level=logging.DEBUG, format='[%(asctime)s] %('
                                                                                                   'levelname)s: %('
                                                                                                   'message)s')

console = Console()


def welcome():
    clear_console()

    logging.info(f"Połączenie zakończone sukcesem. Zalogowany jako {radio_conf['OPERATOR']} - {radio_conf['CALLSIGN']}")

    console.print(Panel(Text("\nZalogowano pomyślnie!\n"
                             f"\nUżytkownik: {radio_conf['OPERATOR']}"
                             f"\nZnak wywoławczy: {radio_conf['CALLSIGN']}\n", justify="center", style="white"),
                        style=get_color("green"), title=f"{frame_title}Menu główne"))

    # It just better look with that.
    time.sleep(0.5)
