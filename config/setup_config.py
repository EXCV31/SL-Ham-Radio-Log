import configparser
import logging
from helpers.colors import get_color
logging.basicConfig(filename='SL_Ham_Radio.log', encoding='utf-8', level=logging.DEBUG, format='[%(asctime)s] %('
                                                                                               'levelname)s: %('
                                                                                               'message)s')


def parse_config():
    """
    Function used to parse the config/config.ini file,
    and set the frame_title variable, displayed on each panel (Rich.Panel)

    Returns:

    """
    # Set configparser and read config.
    logging.info("Parsowanie config.ini...")
    config = configparser.ConfigParser()
    config.read("config/config.ini")

    # Check if config.ini is valid.
    try:
        radio_conf = config['RADIO']
        radio_conf['OPERATOR']
        radio_conf['CALLSIGN']
    except KeyError:
        logging.error("Błąd parsowania config.ini")

        # BaseException instead helpers/error_handler, because frame_title is not initialized.
        raise BaseException("Plik konfiguracyjny jest uszkodzony lub nie został poprawnie wypełniony.")

    logging.info("Parsowanie ukończone.")

    # Setup frame title: display <orange>SL Ham Radio Log <white>- <red>{callsign}<white>- <blue>
    frame_title = f"[{get_color('bold_orange')}]SL Ham Radio Log [{get_color('white')}]" \
                  f"- [{get_color('bold_red')}]{radio_conf['CALLSIGN']}" \
                  f" [{get_color('bold_white')}]- [{get_color('blue')}]"

    return radio_conf, frame_title


radio_conf, frame_title = parse_config()
