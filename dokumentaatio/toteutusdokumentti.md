# Toteutus

## Ohjelman rakenne
Ohjelman toteutus jakautuu pääasiallisesti kahteen kooditiedostoon. `demo.py` toteuttaa käyttöliittymän, `rsalib.py`-kirjasto toteuttaa varsinaiset työssä käytetyt algoritmit ja muut metodit.

`rsalib.py` sisältö:
- `eratostheneen_seula`, `miller_rabin_iteration`, ja `miller_rabin` toteuttavat varsinaiset algoritmit
- `generate_keypair` toteuttaa RSA:ssa käytettyjen avainten luonnin alkuluvuista.
- `get_random_n_bit_prime` on varsinainen metodi jolta muut ohjelmat voivat kutsua pyytääkseen n-bittisen alkuluvun etsimistä kirjastolta.
- RSA-salaus ja merkkijonoenkoodaus toteutetaan pienillä metodeilla `encrypt`, `decrypt`, `encode` ja `decode`.



## Aikavaativuudet
Oletetut aikavaativuudet algoritmeille kirjallisuudessa:
- **Eratostheneen seula**: $O(n \ log \ log \ n)$, jossa $n$ yläraja haettaville alkuluvuille
- **Miller-Rabin**: $O(k \ log³ \ n)$, jossa $n$ testattavan luvun pituus ja $k$ suoritettavien iteraatioiden määrä

Toteutuneet aikavaativuudet:
- **Eratostheneen seulan** aikavaatimus vaikuttaa vastaavaan esitettyä $O(n \ log \ log \ n)$. Toteutus on suhteellisen lähellä Wikipediassa esitettyä pseudokoodikuvausta.

- **Miller-Rabin -algoritmi** vaikuttaa vastaavan myös esitettyä $O(k \ log³ \ n)$. Koodin perusteella pitäisi toteuttaa aikavaatimus, mutta kokeellisesti testatessa tämä pätee lähinnä kun testattavan luvun koko on väliltä 200-6000 bittiä. Suuremilla ja pienemmillä syötteillä käyttäytyy erikoisesti, oletan tämän johtuvan ainakin osittain Pythonista. Testattu kokeellisesti suorittamalla algoritmi useita kertoja erikokoisille syötteille käyttäen k=40, ja vertaamalla keskiarvoisista suoritusajoista muodostuvaa käyrää graafisella laskimella laskettua käyrää vasten.


## Optimointi ja mahdolliset kehityskohteet 

Ohjelman tehokkuutta on mitattu [nopeustestaus](https://github.com/e11-0a/hy-tiralabra-rsa/blob/main/dokumentaatio/nopeustestaus.md)-dokumentissa. Tämän testauksen perusteella suurin osa suoritusajasta kuluu Miller-Rabin iteraatioiden suorittamiseen (noin 15963-641033 µs riippuen lopputuloksesta). Kokeilin ohjelman kehityksen yhteydessä monisäikeistää Miller-Rabin iteraatioiden suorituksen, tämä johti suureen suoritusnopeuden kasvuun. En toteuttanut tätä lopullisessa versiossa, sillä säikeiden pysäyttäminen tuotti ongelmia ohjelman vakaudelle (kun yksi säikeistä on todennut luvun olevan komposiittiuku, pitäisi muut säikeet pysäyttää ja siirtyä toisen luvun testaamiseen). Tämän ongelman voisi mahdollisesti kiertää antamalla säikeiden suorittaa iteraation loppuun, ja testaamalla uutta lukua vain osalla säikeistä sillä aikaa, mutta en pitänyt tätä ratkaisua riittävän "siistinä".

Kokeilin myös vaihtehtoisia Python-ympäristöjä, PyPy:n käyttö nosti suoritusnopeutta noin kolminkertaiseksi (tämä tosin vaatii formatoitujen merkkijonojen muokkaamista, sillä toteutushetkellä PyPy on yhteensopiva vasta Python 3.11 kanssa).

Koodin rakennetta voitaisiin parantaa. Koodi on mielestäni luettavaa, mutta voisi olla siistimpää. Myös tyyppiannotaatiot lopuille metodeille ja muuttujille.

Käyttöliittymä voisi ottaa syötteen myös interaktiivisesti kometoriviargumenttien lisäksi.

## Laajojen kielimallien käyttö
Ei ole käytetty.

## Lähteet
**Ohjelman toteutuksessa käytetyt lähteet:**
<br>
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
<br>
https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
<br>
https://en.wikipedia.org/wiki/RSA_cryptosystem
<br>
https://fi.wikipedia.org/wiki/RSA
<br>
https://www.rfc-editor.org/rfc/rfc8017

**Testauksessa käytetyt alkuluvut:**
<br>
https://www.mersenne.org/
<br>
https://oeis.org/wiki/Mersenne_primes
<br>
https://en.wikipedia.org/wiki/Mersenne_prime
<br>
https://en.wikipedia.org/wiki/List_of_Mersenne_primes_and_perfect_numbers
<br>

10.1090/S0025-5718-52-99405-2
<br>
10.1090/S0025-5718-52-99389-7
<br>
10.1090/S0025-5718-53-99372-7
<br>
10.1090/S0025-5718-58-99282-2