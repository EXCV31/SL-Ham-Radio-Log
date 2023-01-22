import datetime


def get_today():
    """
    Return current day.

    Returns:
        today: Today in format DD-MM-YYYY

    """
    # Get and format current date
    now = datetime.datetime.now()
    today = now.strftime("%d-%m-%Y")

    return today
