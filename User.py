from ecdsa import SigningKey, VerifyingKey, SECP256k1, BadSignatureError
from ecdsa.util import PRNG
from hashlib import sha256, sha3_256
from time import time
import random


def account_create(name):
    t = time()
    hash = sha256()
    hash3 = sha3_256()
    a = str(time())
    b = str(random.random())
    hash.update((a + name + b).encode('utf8'))
    print(a, b, name)
    hash3.update(hash.hexdigest().encode())
    rng = PRNG(hash3.hexdigest())
    sk = SigningKey.generate(curve=SECP256k1, entropy=rng)
    vk = sk.get_verifying_key()
    open("Account\\" + name + '_private.pem', 'wb').write(sk.to_pem())
    open("Account\\" + name + '_public.pem', 'wb').write(vk.to_pem())


def sign(name, message):
    sk = SigningKey.from_pem(open("Account\\" + name + "_private.pem").read())
    hash = sha256(message.encode('utf-8'))
    sig = sk.sign(hash.hexdigest().encode())
    return sig.hex()


def verify(vk, message, signature):
    # vk = VerifyingKey.from_pem(open("Account\\" + name + "_public.pem").read())
    # print(vk.to_string())
    vk = VerifyingKey.from_string(bytes.fromhex(vk), curve=SECP256k1)
    hash = sha256(message.encode('utf8'))
    try:
        if vk.verify(bytes.fromhex(signature), hash.hexdigest().encode()):
            return True
    except BadSignatureError:
        return False


if __name__ == "__main__":
    account_create('zc')
    data = {}
    data['from'] = 'aaaaaa'
    data['to'] = 'bbbbbb'
    data['num'] = 265
    print(str(data))
    sig = sign('zc', str(data))

    name = 'zc'
    vk = VerifyingKey.from_pem(open("Account\\" + name + "_public.pem").read())
    # print(vk.to_string().encode('utf-8'))
    aa = vk.to_string().hex()

    print(sig, len(sig))
    print(aa, len(aa))
    # print(str(aa, encoding="gb18030"))
    print(verify(aa, str(data), sig))
