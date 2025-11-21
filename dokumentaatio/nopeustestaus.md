# Nopeustestaus

Testasin alkulukujakamisen suoritustehokkuutta tehokkuutta, mittasin kuinka pitkään yhden iteraation ajaminen kestää kaikilla alkuluvuilla $n < 10000$ alkuluvuilla.
Taulukossa tulokset 4849 iteraatiosta 2048-bittisillä alkulukukandidaateilla, joista 4212 johti komposiittilukutulokseen ja 637 alkulukutulokseen.

|           | Ei alkuluku | Kyllä alkuluku |
|-----------|-------------|----------------|
| Keskiarvo | 8.08 µs     | 294.61 µs      |
| Minimi    | 0.52 µs     | 287.83 µs      |
| Maksimi   | 291.498 µs  | 376.12 µs      |

Tulokset Miller-Rabin algoritmille alla. Tässä suoritettu 637 iteraatiota koko algoritmia, joista 627 johti komposiittilukutulokseen ja 10 johti alkulukutulokseen.
Huom. Algoritmi oli ohjeiden mukaan konfiguroitu suorittaamaan 40 iteraatiota ennen positiivisen alkulukutuloksen hyväksymistä.

|           | Ei alkuluku     | Kyllä alkuluku |
|-----------|-----------------|----------------|
| Keskiarvo | 15963.71 µs     | 641033.81 µs   |
| Minimi    | 15517.65 µs     | 626036.30 µs   |
| Maksimi   | 17052.53 µs     | 649779.41 µs   |

Alkulukujakamisen suoritusaikavaikutus vaikuttaisi olevan suhteellisen minimaalinen verrattuna Miller-Rabin algoritmiin, vaikkakin jaetaan kaikilla $n < 10000$ alkuluvuilla. (Lopussa oleva cProfile eri ajosta vaikuttaisi tukevan tätä)

Ote cProfile profiloinnista. `prime_division` on alkulukujakaminen.
```
152708 function calls (152675 primitive calls) in 21.199 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      4/1    0.000    0.000   21.200   21.200 {built-in method builtins.exec}
        1    0.002    0.002   21.200   21.200 timings.py:1(<module>)
       10    0.002    0.000   21.192    2.119 timing_rsalib.py:128(get_random_n_bit_prime)
     7693    0.007    0.000   21.190    0.003 timing_rsalib.py:89(try_random_n_bit_prime)
    18882   20.832    0.001   20.832    0.001 {built-in method builtins.pow}
      900    0.002    0.000   20.822    0.023 timing_rsalib.py:68(miller_rabin)
     1290    0.002    0.000   20.820    0.016 timing_rsalib.py:42(miller_rabin_iteration)
     7693    0.325    0.000    0.327    0.000 timing_rsalib.py:97(prime_division)
     7693    0.004    0.000    0.035    0.000 timing_rsalib.py:7(random_n_bit_int)
     8983    0.006    0.000    0.016    0.000 random.py:295(randrange)
     8983    0.003    0.000    0.008    0.000 random.py:245(_randbelow_with_getrandbits)
     9514    0.004    0.000    0.004    0.000 {method 'getrandbits' of '_random.Random' objects}
```

Kaikki testit suoritetty Pythonin versiolla `3.13.7` ja samalla x86_64 arkkitehtuurin Linux koneella.