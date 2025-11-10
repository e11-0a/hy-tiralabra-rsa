import random


def random_n_bit_int(bits: int) -> int:
    """Luo satunnaisen n-bittisen luvun"""
    return random.randrange(pow(2, bits - 1)+1, pow(2, bits))


def eratostheneen_seula(n: int) -> list[int]:
    """Tämä metodi toteuttaa eratostheneen seulan, jonka avulla lasketaan alkulukulista 
    esiseulontaa varten. (seulotaan komposiittilukuja pois ennen Miller-Rabinin ajoa)"""

    # Matematiikka peräisin wikipediasta
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    a = [True]*n
    a[0:1] = [False]*2
    primes = []

    i = 2
    while i <= n:
        if a[i]:
            j = i*i
            while j <= n:
                a[j] = False
                j += i
        i += 1

    for j, x in enumerate(a):
        if x:
            primes.append(j)

    return primes


primes: list[int] = eratostheneen_seula(10000)


def miller_rabin_iteration(candidate: int, d: int, s: int) -> bool:
    """Metodi toteuttaa iteraation Miller-Rabinin algoritmia. """
    # Arvotaan satunnaisluku
    a = random.randint(2, candidate - 2)

    # Nostetaan satunnaisluku d:teen potensiin ja otetaan lopputuloksen modulo
    # kandidaattiluvulla
    x = pow(a, d, candidate)

    # On alkuluku joten palautetaan suoraan
    if (x == 1) or (x == candidate - 1):
        return True 

    y = 0
    for _ in range(s):
        y = pow(x, 2, candidate)
        # Testit ohitettu, koska vaatii satunnaisluvun osuvan kohdalle
        if (y == 1) and (x != 1) and (x != candidate - 1): # pragma: no cover
            return False
        x = y
    if y != 1:
        return False

    return True # pragma: no cover


def miller_rabin(candidate: int, rounds: int) -> bool:
    """Metodi joka toteuttaa Miller-Rabinin halutulle alkulukukandidaatille 
    halutun määrän iteraatioita"""

    d = candidate - 1
    s = 0

    while ((d % 2) == 0):
        s += 1
        d = d // 2

    # Toistetaan miller-rabinia pyydetyn määrän iteraatioita verran
    for _ in range(rounds):
        # Jos algoritmi toteaa edes kerran että luku ei ole alkuluku,
        # lopetetaan tarkistusprosessi ja palataan arpomaan uusi luku
        result = miller_rabin_iteration(candidate, d, s)
        if result != True:
            return False
    return True


def try_random_n_bit_prime(bits: int) -> int | None:
    """Varsinainen metodi jolla etsitään n-bittinen alkuluku"""

    candidate = random_n_bit_int(bits)

    # Varmista että on pariton
    candidate += not candidate % 2

    # Testataan alkulukukandidaatin jaollisuutta tunnetuilla pienillä alkuluvuilla
    for i in primes:
        res = candidate % i
        if res == 0:
            return None

    # Suoritetaan Miller-Rabin kandidaattialkuluvulle
    mres = miller_rabin(candidate, 5)

    if not mres:
        return None

    return candidate


def get_random_n_bit_prime(bits: int) -> int:
    """Tältä metodilta on tarkoitus pyytää alkuluku muissa ohjelmissa """
    prime_res = None
    while prime_res == None:
        prime_res = try_random_n_bit_prime(bits)
    return prime_res


def generate_keypair(p: int, q: int) -> tuple[tuple[int, int], tuple[int, int]]:
    """
    Tämä metodi luo RSA-avainparin kahdesta alkuluvusta

    Muuttujien selite:
    q ja p = alkuluvut (täytyy salata)
    e = julkinen eksponentti
    N = modulus
    d = yksityinen eksponentti (täytyy salata)
    phi = asia (täytyy salata)
    avain = (modulus, eksponentti)
    """

    # Matematiikka perustuu wikipediaan
    # https://fi.wikipedia.org/wiki/RSA

    N = p * q
    e = 65537  # voisi olla myös 3, 17 jne. Pienemmät on nopeampia laskea, mutta heikompia
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)

    public_key = (N, e)
    private_key = (N, d)

    return public_key, private_key


def encrypt(data, e, N):
    return pow(data, e, N)


def decrypt(data, d, N):
    return pow(data, d, N)


def encode(text): return int(
    '1'+''.join(list(map(lambda x: f"{min(ord(x)-32, 99):02}", text))))


def decode(data): return ''.join(
    [chr(int(str(data)[1:][x:x+2])+32) for x in range(0, len(str(data))-1, 2)])
