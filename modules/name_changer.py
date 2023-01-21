from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import logging

# File imports
from database.setup_db import cursor, conn
from config.setup_config import frame_title
from helpers.error_handler import display_error

console = Console()

def change_or_add_name():
    qso_callsign = input("\nPodaj znak swojego rozmówcy (pozostaw puste aby wyjść): ")
    if qso_callsign == "":
        return

    # sprawdzenie czy znak istnieje w bazie danych
    cursor.execute("SELECT ZNAK FROM IMIONA WHERE ZNAK=?", (qso_callsign,))
    result = cursor.fetchone()

    if result:

        # znak istnieje w bazie
        new_name = input("Znak istnieje w bazie. Podaj nowe imię: ")
        if new_name == "":
            display_error("Imię nie może być puste!")
        cursor.execute("UPDATE IMIONA SET IMIE=? WHERE ZNAK=?", (new_name, qso_callsign))
        conn.commit()
        print("Imię zostało zmienione.")
    else:
        # znak nie istnieje w bazie
        name = input("Znaku nie ma w bazie. Podaj imię: ")
        if name == "":
            display_error("Imię nie może być puste!")
        cursor.execute("INSERT INTO IMIONA (IMIE, ZNAK) VALUES (?, ?)", (name, qso_callsign))
        conn.commit()
        print("Imię zostało dodane do bazy.")