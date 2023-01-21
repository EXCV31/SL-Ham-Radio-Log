from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import logging

# File imports
from database.setup_db import cursor, conn
from helpers.colors import get_color
from config.setup_config import frame_title
from helpers.get_today_or_yesterday import get_time
from helpers.bands import match_band
from helpers.modulations import match_modulation

console = Console()
logging.basicConfig(filename='SL_Ham_Radio_Log.log', encoding='utf-8', level=logging.DEBUG, format='[%(asctime)s] %('
                                                                                                   'levelname)s: %('
                                                                                                   'message)s')


def register_qso():
    """
    The function is responsible for registering QSO by putting it inside database.
    Returns:
    """
    while True:
        qso_callsign = input("\nPodaj znak swojego rozmówcy (pozostaw puste aby wyjść): ")
        if qso_callsign == "":
            return

        # Check if name of operator exists in database
        cursor.execute("SELECT IMIE FROM IMIONA WHERE ZNAK=?", (qso_callsign,))
        result = cursor.fetchone()

        # Przypisanie do zmiennej
        if result:
            name = result[0]
        else:
            name = input("Podaj imię rozmówcy (opcjonalne, można zostawić puste): ")
            if name != "":
                cursor.execute("INSERT INTO IMIONA (ZNAK, IMIE) VALUES (?, ?)", (qso_callsign, name))

        console.print("", Panel(Text(f"\nWybrano znak: {qso_callsign}"
                                    f"\nImię rozmówcy: {name}\n", justify="center", style="white"),
                                style=get_color("light_blue"), title=frame_title),
                    "")
        logging.info(f"Wybrano znak: {qso_callsign}")

        console.print(Panel(Text("\n "
                                "1. 160m   1.810 MHz - 2.000 MHz\n"
                                "2. 80m   3.500 MHz - 3.800 MHz\n"
                                "3. 40m   7.000 MHz - 7.200 MHz\n"
                                "4. 30m   10.100 MHz - 10.150 MHz\n"
                                "5. 20m   14.000 MHz - 14.350 MHz\n"
                                "6. 17m   18.068 MHz - 18.168 MHz\n"
                                "7. 15m   21.000 MHz - 21.450 MHz\n"
                                "8. 12m   24.890 MHz - 24.990 MHz\n"
                                "9. 10m   28.000 MHz - 29.700 MHz\n"
                                "10. 6m   50.000 MHz - 52.000 MHz\n"
                                "11. 2m    144.000 MHz - 146.000 MHz\n"
                                "12. 70cm   430.000 MHz - 440.000 MHz\n", justify="center", style="white"), style=get_color("light_blue")
                            , title=frame_title))
        band = input("\nWybierz numer pasma, lub wpisz własne: ")

        band = match_band(band)

        console.print(Panel(Text("\n "
                        "1. FM\n"
                        "2. CW\n"
                        "3. RTTY\n"
                        "4. FT4\n"
                        "5. FT8\n"
                        "6. SSB/LSB/USB\n"
                        "7. DMR\n"
                        "8. FUSION\n"
                        "9. D-STAR\n", justify="center", style="white"), style=get_color("light_blue")
                    , title=frame_title))
        modulation = input("\nWybierz numer modulacji, lub wpisz własną: ")

        modulation = match_modulation(modulation)

        today = get_time()

        # Insert user work to database.
        cursor.execute("INSERT INTO QSO (DATA, ZNAK, PASMO, MODULACJA) VALUES (?,?,?,?)", (today, qso_callsign, band, modulation))
        conn.commit()

        logging.info("Umieszczono przepracowany czas w bazie danych.")

        # Apply changes and close connection to sqlite database.
        conn.commit()
        logging.info("Zacommitowano zmiany w bazie danych.")

        console.print("", Panel(Text(f"\nDodano!\n", justify="center", style="white"),
                                style=get_color("green"), title=frame_title), "")
        
# WYMAGA REFAKTORYZACJI, DZIAŁA, NIE PRZETESTOWANE W 100%