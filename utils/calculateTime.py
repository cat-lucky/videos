def calculateTime(seconds):
    if seconds == 0:
        return "Unknown"
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    if hours == 0 and minutes == 0:
        return f"{seconds}s"
    elif hours == 0 and seconds == 0:
        return f"{minutes}m"
    elif minutes == 0 and seconds == 0:
        return f"{hours}h"
    elif hours == 0:
        return f"{minutes}m {seconds}s"
    elif minutes == 0:
        return f"{hours}h {seconds}s"
    elif seconds == 0:
        return f"{hours}h {minutes}m"
    return f"{hours}h {minutes}m {seconds}s"
