import requests
import random
import time
import User
from ecdsa import VerifyingKey


def getblock():
    nodefile = open('nodes.txt')
    nodes = nodefile.readlines()
    nodefile.close()
    for i in range(len(nodes)):
        print(nodes[i][:-1] + "/getblock")
        try:
            response = requests.get(nodes[i][:-1] + "/getblock")
            print(response.text)
        except:
            continue
        block_new = response.text


if __name__ == '__main__':
    nodefile = open('nodes.txt')
    nodes = nodefile.readlines()
    nodefile.close()

    name = 'aaa'
    vk = VerifyingKey.from_pem(open("Account\\" + name + "_public.pem").read()).to_string().hex()
    data = {'from': vk, 'to': 'bbb', 'num': 15, 'flg': 1}
    print(data)
    sig = User.sign('aaa', str(data))
    print(User.verify(vk, str(data), sig))
    data['sig'] = sig

    for i in range(len(nodes)):
        print(nodes[i][:-1] + "/submittrans")
        try:
            response = requests.get(nodes[i][:-1] + "/submittrans", params=data)
            print(response.text)
        except:
            continue
        block_new = response.text
