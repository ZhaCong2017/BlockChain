def _init():
    global new_block_found
    global block_list
    global trans_list
    new_block_found = False
    block_list = {}
    trans_list = []


def set_value(value):
    new_block_found = value


def get_value():
    return new_block_found


def appendtrans(data):
    trans_list.append(data)


def get_parentblockhash():
    n = len(block_list)
    return block_list[n - 1]['hash']


