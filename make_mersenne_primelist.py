def n_bit(x): return pow(2, x)
def calc_prime(p): return pow(2, p)-1


lower = n_bit(500)
upper = n_bit(4000)


# https://www.mersenne.org/primes/
# https://oeis.org/wiki/Mersenne_primes
# https://en.wikipedia.org/wiki/List_of_Mersenne_primes_and_perfect_numbers
# 10.1090/S0025-5718-52-99405-2
# 10.1090/S0025-5718-52-99389-7
# 10.1090/S0025-5718-53-99372-7
# 10.1090/S0025-5718-58-99282-2

known_mersenne_exponents = [
    2,
    3,
    5,
    7,
    13,
    17,
    19,
    31,
    61,
    89,
    107,
    127,
    521,
    607,
    1279,
    2203,
    2281,
    3217,
    4253,
    4423,
    9689,
    9941,
    11213,
    19937,
    21701,
    23209,
    44497,
    86243,
    110503,
    132049,
    216091,
]

primes = list(filter(lambda x: (x > lower) and (x < upper), [
    calc_prime(i) for i in known_mersenne_exponents
]))


for i in primes:
    print(i)