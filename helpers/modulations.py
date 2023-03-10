def match_modulation(modulation):
    match modulation:
        case "1":
            return "FM"
        case "2":
            return "CW"
        case "3":
            return "RTTY"
        case "4":
            return "FT4"
        case "5":
            return "FT8"
        case "6":
            return "SSB/USB/LSB"
        case "7":
            return "DMR"
        case "8":
            return "FUSION"
        case "9":
            return "D-STAR"
        case _:
            return modulation
