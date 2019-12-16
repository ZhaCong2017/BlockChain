import User
from ecdsa import VerifyingKey


def _init():
    global account_flg
    global account_number

    #test
    name = 'aaa'
    User.account_create(name)
    vk = VerifyingKey.from_pem(open("Account\\" + name + "_public.pem").read()).to_string().hex()
    #test

    account_flg = {}
    account_number = {vk: 100}


def increase_number(account, number):
    if account in account_number:
        account_number[account] += number
    else:
        account_number[account] = number
        account_flg[account] = set()


def get_number(account):
    if account in account_number:
        return account_number[account]
    else:
        return -1


def get_flg(account, flg):
    if account not in account_flg:
        return False
    if flg in account_flg[account]:
        return True
    else:
        return False
