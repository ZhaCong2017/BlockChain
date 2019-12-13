from ecdsa import SigningKey, VerifyingKey, NIST384p, BadSignatureError
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
    sk = SigningKey.generate(curve=NIST384p, entropy=rng)
    vk = sk.get_verifying_key()
    open("Account\\" + name + ' ' + a + '_private.pem', 'wb').write(sk.to_pem())
    open("Account\\" + name + ' ' + a + '_public.pem', 'wb').write(vk.to_pem())


def sign(name, message):
    sk = SigningKey.from_pem(open("Account\\" + name + "_private.pem").read())
    hash = sha256()
    hash.update(message.encode('utf8'))
    sig = sk.sign(hash.hexdigest().encode())
    return sig


def verify(name, message, signature):
    vk = VerifyingKey.from_pem(open("Account\\" + name + "_public.pem").read())
    hash = sha256()
    hash.update(message.encode('utf8'))
    try:
        if vk.verify(signature, hash.hexdigest().encode()):
            return True
    except BadSignatureError:
        return False


if __name__ == "__main__":
    account_create('zc')
    sig = sign('zc', "天朗气清，惠风和畅")
    print(verify('zc', "天朗气清，惠风和畅", sig))
