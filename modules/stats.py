from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import logging

# File imports
from config.setup_config import frame_title
from database.setup_db import cursor, conn
from helpers.colors import get_color


console = Console()


def show_stats():
    stats = ""
    # zapytanie najczęściej występującego znaku
    cursor.execute("SELECT ZNAK, COUNT(ZNAK) FROM QSO GROUP BY ZNAK ORDER BY COUNT(ZNAK) DESC LIMIT 1")
    result = cursor.fetchone()
    stats += f"Ulubiony znak: {result[0]}, {result[1]} QSO\n"

    # zapytanie najczęściej występującego pasma
    cursor.execute("SELECT PASMO, COUNT(PASMO) FROM QSO GROUP BY PASMO ORDER BY COUNT(PASMO) DESC LIMIT 1")
    result = cursor.fetchone()
    stats += f"Ulubione pasmo: {result[0]}, {result[1]} QSO\n"

    # zapytanie najczęściej występującej modulacji
    cursor.execute("SELECT MODULACJA, COUNT(MODULACJA) FROM QSO GROUP BY MODULACJA ORDER BY COUNT(MODULACJA) DESC LIMIT 1")
    result = cursor.fetchone()
    stats += f"Ulubiona modulacja: {result[0]}, {result[1]} QSO\n"

    # zapytanie najczęściej występującej daty
    cursor.execute("SELECT DATA, COUNT(DATA) FROM QSO GROUP BY DATA ORDER BY COUNT(DATA) DESC LIMIT 1")
    result = cursor.fetchone()
    stats += f"Najbardziej aktywny dzień: {result[0]}, {result[1]} QSO"
    console.print(Panel(Text(f"\n {stats} \n", justify="center", style="white"), style=get_color("light_blue")
                            , title=f"{frame_title}Statystyki"))