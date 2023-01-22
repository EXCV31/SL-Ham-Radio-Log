from rich.console import Console
from rich.panel import Panel
from rich.text import Text

# File imports
from config.setup_config import frame_title
from helpers.colors import get_color

console = Console()


def show_about():
    console.print(Panel(Text("\n "
                             "SL Ham Radio Log. W założeniu prosty program służący do rejestrowania łączności. "
                             "Wiadomo, z czasem projekt spuchnął, pojawiło się sporo funkcjonalności. "
                             "Cały program powstał w raptem kilka dni, bardzo tutaj pomógł fakt, "
                             "że ten program to tak naprawdę przerobiony poprzedni projekt, zwany CZASOINATOR.\n\n"
                             "Szczególne podziękowania dla najlepszego klubu krótkofalarskiego "
                             "SP9KUP w Andrychowie za przygotowanie do egzaminu i godziny spędzone w klubie "
                             "gadając o wszystkim i o niczym, oraz dla mojej narzeczonej za wsparcie i kopanie kiedy "
                             "mi się nie chciało pracować nad tym programem.", justify="center", style="white"),
                        style=get_color("light_blue"), title=f"{frame_title}O programie"))
