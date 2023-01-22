import logging
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from helpers.colors import get_color
from config.setup_config import frame_title

logging.basicConfig(filename='SL_Ham_Radio.log', encoding='utf-8', level=logging.DEBUG, format='[%(asctime)s] %('
                                                                                               'levelname)s: %('
                                                                                               'message)s')
console = Console()


def display_error(text):
    """
    Function used for displaying errors - normal and critical. Often used before helpers/exit_handler.py
    Args:
        text: Text of error displayed in frame.

    Returns:

    """
    print("")
    console.print(
        Panel(Text(f"\n{text}\n", justify="center", style="white"), style=get_color("red"), title=f"{frame_title}Błąd"))
    logging.error(text)
