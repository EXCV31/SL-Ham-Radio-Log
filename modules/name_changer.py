from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import logging

# File imports
from database.setup_db import cursor, conn
from config.setup_config import frame_title
from helpers.error_handler import display_error
from helpers.colors import get_color

console = Console()

logging.basicConfig(filename='SL_Ham_Radio_Log.log', encoding='utf-8', level=logging.DEBUG, format='[%(asctime)s] %('
                                                                                                   'levelname)s: %('
                                                                                                   'message)s')


def change_or_add_name():
    console.rule(f"[{get_color('bold_orange')}] {frame_title}Zmień imię", )

    qso_callsign = input("\nPodaj znak swojego rozmówcy (pozostaw puste aby wyjść): ")
    if qso_callsign == "":
        return

    # Check if callsign exists in database
    cursor.execute("SELECT ZNAK FROM IMIONA WHERE ZNAK=?", (qso_callsign,))
    result = cursor.fetchone()

    if result:

        # Callsign exist in database.
        new_name = input("Znak istnieje w bazie. Podaj nowe imię: ")

        if new_name == "":
            display_error("Imię nie może być puste!")

        cursor.execute("UPDATE IMIONA SET IMIE=? WHERE ZNAK=?", (new_name, qso_callsign))
        conn.commit()
        logging.info(f"Zmieniono imię w bazie dla znaku {qso_callsign}")
    else:
        # Callsign doesn't exist in database.
        name = input("Znaku nie ma w bazie. Podaj imię: ")
        if name == "":
            display_error("Imię nie może być puste!")
        cursor.execute("INSERT INTO IMIONA (IMIE, ZNAK) VALUES (?, ?)", (name, qso_callsign))
        conn.commit()
        logging.info(f"Dodano imię w bazie dla znaku {qso_callsign}")
    print("")
    console.print(Panel(Text("\nDodano!\n", justify="center", style="white"),
                        style=get_color("light_blue"), title=f"{frame_title}Zmień imię"))
