import sys
import rsalib

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
    fprint(f"[FAIL]Not enough args[ENDC]")
    exit(1)

output = sys.argv[2]

try:
    key_length = int(sys.argv[1])
except ValueError as e:
    fprint(f"[FAIL]Invalid key length '{sys.argv[1]}'[ENDC]")


p = rsalib.get_random_n_bit_prime(key_length)
q = rsalib.get_random_n_bit_prime(key_length)

keypair = rsalib.generate_keypair(p, q)

N = keypair[0]
e = keypair[1]
d = keypair[2]

serialized_keypair = '|'.join([str(N), str(e), str(d)])

f = open(output, "w")
f.write(serialized_keypair)
f.close()