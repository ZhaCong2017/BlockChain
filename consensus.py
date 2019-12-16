from hashlib import sha256
import time
import globalvar as g

difficulty_to_aim = {1: 7, 2: 3, 3: 1}


def make_Merkletree(transactions):
    hash = [0] * len(transactions)
    for i in range(len(transactions)):
        hash[i] = sha256(transactions[i].encode('utf8'))
    # for i in hash:
    #     print(i, i.hexdigest())

    while len(hash) != 1:
        hash_base = hash
        n = int((len(hash_base) + 1) / 2)
        hash = [0] * n
        for i in range(n - 1):
            hash[i] = sha256((hash_base[i * 2].hexdigest() + hash_base[i * 2 + 1].hexdigest()).encode('utf8'))
        if len(hash_base) % 2 == 1:
            hash[-1] = hash_base[-1]
        else:
            hash[-1] = sha256((hash_base[-2].hexdigest() + hash_base[-1].hexdigest()).encode('utf8'))
        # for i in hash:
        #     print(i.hexdigest())
        # print("  ")
    return hash[0].hexdigest()


def get_parentblockhash():
    return "aaaaaaaaa"


def mining(transactions, my_account, height_now):
    block = {}
    block['parent block hash'] = get_parentblockhash()
    block['height'] = height_now + 1
    block['Merkle tree'] = make_Merkletree(transactions)
    block["miner"] = my_account
    block['time'] = time.time()
    block['difficulty'] = 40
    block['Nonce'] = 0

    num = int(block['difficulty'] / 4)
    flag = False
    if block['difficulty'] % 4 == 0:
        flag = True
    aim = '0' * num
    while True:
        if g.get_value():
            return -1
        hash = sha256(bytes('{}'.format(block), 'utf-8'))
        # print(block['Nonce'], hash.hexdigest())
        if hash.hexdigest()[:num] == aim:
            if flag:
                break
            elif int(hash.hexdigest()[num], 16) <= difficulty_to_aim[block['difficulty'] % 4]:
                break
        block['Nonce'] += 1

    block['hash'] = hash.hexdigest()
    block['number'] = len(transactions)
    block['transactions'] = transactions
    print(block['Nonce'], hash.hexdigest())
    print(block)
    return block


if __name__ == '__main__':
    transactions = ['1', '2', '3', '4', '5', '9']
    # result = make_Merkletree(transactions)
    # print(result)

    mining(transactions)
