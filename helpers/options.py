from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import logging

# File imports
from config.setup_config import radio_conf, frame_title
from helpers.colors import get_color

console = Console()
logging.basicConfig(filename='czasoinator.log', encoding='utf-8', level=logging.DEBUG, format='[%(asctime)s] %('
                                                                                              'levelname)s: %('
                                                                                              'message)s')


def show_options():
    """
    Point where program start with user interaction.

    Returns:

    """

    console.print(Panel(Text("\nWybierz co chcesz zrobić:\n"
                             "\n1. Zarejestruj QSO"
                             "\n2. Sprawdź najczęstsze łączności - TOP 10"
                             "\n3. Sprawdź ilość QSO z znakiem"
                             "\n4. Zmień lub dodaj imię dla znaku"
                             "\n5. Statystyki"
                             "\n6. O programie"
                             "\n7. Wyjście"
                             "\n?. Pokaż to menu\n", justify="center", style="white"), style=get_color("light_blue"),
                        title=f"{frame_title}Menu główne"))
    logging.info("Pokazano listę opcji do wyboru.")
