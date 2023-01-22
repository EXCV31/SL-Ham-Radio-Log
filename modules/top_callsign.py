from rich.console import Console
from rich.panel import Panel
from rich.text import Text

# File imports
from config.setup_config import frame_title
from helpers.colors import get_color
from database.setup_db import cursor
from helpers.error_handler import display_error
console = Console()

def show_top_callsign():
    qso_callsign = input("\nPodaj znak swojego rozmówcy (pozostaw puste aby wyjść): ")
    if qso_callsign == "":
        return
    query = "SELECT ZNAK, COUNT(*) FROM QSO WHERE ZNAK = ? GROUP BY ZNAK;"
    cursor.execute(query, (qso_callsign,))

    result = cursor.fetchone()

    if result:
        text = f"\n{result[0]}: {result[1]}\n"
        console.print(Panel(Text(text, justify="center", style="white"), style=get_color("light_blue"), title=f"{frame_title}Ilość QSO"))
    else:
        display_error("Nie znaleziono podanego znaku w bazie.")

# WYMAGA REFAKTORYZACJI + DODANIE LOGGERA, DZIAŁA