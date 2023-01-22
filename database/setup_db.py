import sqlite3
import logging

logging.basicConfig(filename='SL_Ham_Radio.log', encoding='utf-8', level=logging.DEBUG, format='[%(asctime)s] %('
                                                                                               'levelname)s: %('
                                                                                               'message)s')


def setup_connection_and_cursor():
    """
    Setup database, and return conn and cursor object.

    Returns:

    """

    # Set up sqlite connection.
    conn = sqlite3.connect("database/radio_log.db")
    logging.info("Nawiązano połączenie z bazą danych.")
    cursor = conn.cursor()

    return conn, cursor


conn, cursor = setup_connection_and_cursor()
