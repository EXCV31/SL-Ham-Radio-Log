def match_band(band):
    """

    Args:
        band: number of band from list showed to user.

    Returns: matched band from 160m to 70cm.

    """
    match band:
        case "1":
            return "160m"
        case "2":
            return "80m"
        case "3":
            return "40m"
        case "4":
            return "30m"
        case "5":
            return "20m"
        case "6":
            return "17m"
        case "7":
            return "15m"
        case "8":
            return "12m"
        case "9":
            return "10m"
        case "10":
            return "6m"
        case "11":
            return "2m"
        case "12":
            return "70cm"
        case _:
            return band
