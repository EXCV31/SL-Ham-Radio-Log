from rich.console import Console
import logging

# File imports
from helpers.exit_handler import exit_program
from helpers.options import show_options
from modules.qso import register_qso
from modules.top import top_10_connections
from modules.top_callsign import show_top_callsign
from modules.name_changer import change_or_add_name
from modules.stats import show_stats
from modules.about import show_about
from helpers.greet_user import welcome

logging.basicConfig(filename='SL_Ham_Radio_Log.log', encoding='utf-8', level=logging.DEBUG, format='[%(asctime)s] %('
                                                                                                   'levelname)s: %('
                                                                                                   'message)s')

info = False
console = Console()
logging.info("Aplikacja została uruchomiona")

if __name__ == "__main__":
    welcome()

    # Main loop of script. Here we have "info" variable, which store True/False about showing options to choose.
    while True:
        if info is False:
            show_options()
            info = True
    
        choose = input("\nWybór: ")
        
        if choose == str(1):
            register_qso()
        if choose == str(2):
            top_10_connections()
        if choose == str(3):
            show_top_callsign()
        if choose == str(4):
            change_or_add_name()
        if choose == str(5):
            show_stats()
        if choose == str(6):
            show_about()
        if choose == str(7):
            exit_program(0)
        if choose == "?":
            info = False
