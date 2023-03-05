import math
import random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import pandas as pd
import numpy as np


def crypto_rsa():
    keyPair = RSA.generate(1024)

    pubKey = keyPair.publickey()
    print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
    pubKeyPEM = pubKey.exportKey()
    print(pubKeyPEM.decode('ascii'))

    print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
    privKeyPEM = keyPair.exportKey()
    print(privKeyPEM.decode('ascii'))


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num ** 0.5) + 2, 2):
        if num % n == 0:
            return False
    return True


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    n = p * q

    # totient of n
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # multiplicative_inverse(e, phi)
    d = pow(e, -1, phi)

    # Return public and private keypair
    # pub_key = {
    #     "e": e,
    #     "n": n
    # }
    #
    # pri_key = {
    #     "d": d,
    #     "n": n,
    # }

    keys = {
        "e_pub": e,
        "n_pub": n,
        "d_pri": d,
    }

    return keys


if __name__ == '__main__':
    # pub, pri = generate_keypair(61, 53)
    # print(pub)
    # print(pri)
    prime_list = [71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
                  179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
                  283, 293]

    list_of_keys = []
    for i in range(10):
        bases = random.sample(prime_list, 2)
        key_pair = generate_keypair(bases[0], bases[1])
        list_of_keys.append(key_pair)

    key_df = pd.DataFrame(list_of_keys)

    key_df.to_excel("output/key_list_rsa.xlsx", index=False)
    print()


