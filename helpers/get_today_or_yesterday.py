import datetime


def get_time():
    """
    Return current time, yesterday and today. If today is Monday,
    function will return Friday as yesterday.

    Returns:
        current_time: Current time in format YYYY-MM-DD HH:MM:SS
        yesterday: Yesterday in format YYYY-MM-DD
        today: Today in format YYYY-MM-DD

    """
    # Get and format current date
    now = datetime.datetime.now()
    current_time = now.strftime("%d-%m-%Y %H:%M:%S")

    # Split current time from 10-12-2021 22:32:52 to 10-12-2021
    today = current_time.split(" ")[0]

    return today
