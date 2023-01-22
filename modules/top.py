from rich.console import Console
from rich.panel import Panel
from rich.text import Text

# File imports
from config.setup_config import frame_title
from helpers.colors import get_color
from helpers.clear_handler import clear_console
from database.setup_db import cursor

console = Console()


def top_10_connections():
    clear_console()
    query = "SELECT ZNAK, COUNT(*) FROM QSO GROUP BY ZNAK ORDER BY COUNT(*) DESC LIMIT 10;"
    cursor.execute(query)

    results = cursor.fetchall()
    results = "\n".join([f"{result[0]}: {result[1]}" for result in results])

    console.print(Panel(Text(f"\n{results}\n", justify="center", style="white"), style=get_color("light_blue"),
                        title=f"{frame_title}TOP 10 QSO"))
