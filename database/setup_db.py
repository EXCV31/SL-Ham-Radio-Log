import sqlite3
import os

def setup_connection_and_cursor():
    """
    Setup database.

    Returns:

    """
    base_dir = os.path.abspath(os.path.dirname(__file__))
    # Set up sqlite
    conn = sqlite3.connect("database/radio_log.db")
    cursor = conn.cursor()

    return conn, cursor


conn, cursor = setup_connection_and_cursor()
