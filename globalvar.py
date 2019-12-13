def _init():
    global new_block_found
    new_block_found = False


def set_value(value):
    new_block_found = value


def get_value():
    return new_block_found
