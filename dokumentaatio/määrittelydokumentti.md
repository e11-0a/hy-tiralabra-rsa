# Määrittelydokumentti

**Toteutuskieli**: Python
<br>
**Dokumentaatiokieli**: Suomi
<br>
**Vertaisarvioitavat ohjelmointikielet**: Python, JS, C++
<br>
**Vertaisarvioitavat kielet**: Suomi ja Englanti
<br>
**Opinto-ohjelma**: Tietojenkäsittelytieteen kandidaatti (TKT)

Ohjelman tarkoitus on käyttäjän antaman tekstidatan salaaminen ja salauksen purku RSA-salausalgoritmilla. Ohjelman on myös tarkoitus kyetä luomaan salauksessa käytettävät avainparit. 

Harjoitustyön ydin on toteuttaa ohjelma joka toteuttaa RSA-salauksen, sekä siihen vaadittujen avainten luomisen. 
<br>
Ohjelman ytimen toteutukseen kuuluvat seuraavat osat:
1. Ainakin 2048-bittisien alkulukujen etsiminen Eratostheneen seulan ja Miller-Rabinin testin avulla.
2. Julkisen ja yksityisen avaimen luominen alkuluvuista.
3. Käyttää luotua avainparia RSA-salauksen suorittamiseen ja purkamiseen datalle.

### Projektissa toteutettavat algoritmit ja tietorakenteet
- **Eratostheneen seula**
    - Pienien alkulukujen laskeminen
- **Miller–Rabin testi**
    - Testataan onko luku alkuluku, suorittamalla useampia iteraatioita saadaan varmempi tulos
- **RSA**
    - Toteutettava salausalgoritmi

### Aikavaativuudet
- **Eratostheneen seula**: $O(n \ log \ log \ n)$, jossa $n$ yläraja haettaville alkuluvuille
- **Miller-Rabin**: $O(k \ log³ \ n)$, jossa $n$ testattavan luvun pituus ja $k$ suoritettavien iteraatioiden määrä

## Lähteet 

https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
<br>
https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
<br>
https://en.wikipedia.org/wiki/RSA_cryptosystem
<br>
https://fi.wikipedia.org/wiki/RSA
<br>
https://www.rfc-editor.org/rfc/rfc8017