import requests
import random
import time


if __name__ == '__main__':
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
