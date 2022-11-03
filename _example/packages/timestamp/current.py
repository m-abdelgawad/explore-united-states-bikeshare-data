from datetime import datetime


def get_current_timestamp():
    return str(datetime.now().strftime("%Y-%m-%d__%H-%M-%S"))
