#!/usr/bin/python

import rsalib
import sys

'''
Demoskripti rsalibiä varten. 

Käyttö ./demo.py [haluttu avainten bittimäärä] [testattava teksti]

esim.
./demo.py 512 "Hello World"
./demo.py 2048 "This might take a bit longer"
'''

ansicodes = {
    "HEADER":    '\033[95m',
    "BLUE":      '\033[94m',
    "CYAN":      '\033[96m',
    "GREEN":     '\033[92m',
    "WARNING":   '\033[93m',
    "FAIL":      '\033[91m',
    "ENDC":      '\033[0m',
    "BOLD":      '\033[1m',
    "UNDERLINE": '\033[4m'
}


def ansi_string(a):
    for i in ansicodes:
        a = a.replace(f"[{i}]", ansicodes[i])
    return a


def fprint(a):
    print(ansi_string(a))

if len(sys.argv) < 3:
    print("Usage ./demo.py [key length in bits] [text to encrypt]")
    exit(1)

try:
    bits = int(sys.argv[1])
    if bits < 14:
        raise ValueError()
except ValueError:
    fprint("[FAIL]Prime length should a positive integer >= 14[ENDC]")
    exit(1)


'''
Varsinainen demo alkaa tästä. Ylempi lähinnä syötteenvalidointia ja tulosteet formatointia
'''


input_text = sys.argv[2]




fprint(f"Generating two [GREEN]{bits}[ENDC]-bit primes:")

p = rsalib.get_random_n_bit_prime(bits)
q = rsalib.get_random_n_bit_prime(bits)

fprint(f"Prime 1          (p):[GREEN] {p}[ENDC]")
fprint(f"Prime 2          (q):[GREEN] {q}[ENDC]\n")

fprint(f"Generating keypair:")

keypair = rsalib.generate_keypair(p, q)

N = keypair[0]
e = keypair[1]
d = keypair[2]

fprint(f"Modulo           (N):[GREEN] {N}[ENDC]")
fprint(f"Public  exponent (e):[GREEN] {e}[ENDC]")
fprint(f"Private exponent (d):[GREEN] {d}[ENDC]\n")

fprint(f"Encoding message to an integer:")

encoded_text = rsalib.encode(input_text)

fprint(f"Original message    :[GREEN] {input_text}[ENDC]")
fprint(f"Encoded message     :[GREEN] {encoded_text}[ENDC]\n")

fprint("Encrypting the message:")

encrypted_message = rsalib.encrypt(encoded_text, e, N)

fprint(f"Encrypted message   :[GREEN] {encrypted_message}[ENDC]\n")

fprint("Decrypting the message:")

decrypted_message = rsalib.decrypt(encrypted_message, d, N)

fprint(f"Decrypted message   :[GREEN] {decrypted_message}[ENDC]\n")

fprint("Decoding the message:")

decoded_message = rsalib.decode(decrypted_message)

fprint(f"Decoded message     :[GREEN] {decoded_message}[ENDC]\n")

fprint(
    f"The decrypted message matches the original: [BOLD]{["[FAIL]No[ENDC]", "[GREEN]Yes"][decrypted_message == encoded_text]}[ENDC]")
fprint(
    f"The decoded message matches the original  : [BOLD]{["[FAIL]No[ENDC]", "[GREEN]Yes"][decoded_message == input_text]}[ENDC]")
