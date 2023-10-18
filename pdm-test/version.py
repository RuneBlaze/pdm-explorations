from datetime import datetime

def current_year() -> int:
    return datetime.now().year

def random_version() -> str:
    return '0.1.0+' + str(hash(current_year()))

get_version = random_version