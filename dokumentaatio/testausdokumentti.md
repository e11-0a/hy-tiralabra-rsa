# Testaus

Ohjelmaa (`rsalib.py`) testataan kokonaisuutena (päästä-päähän testaus), sekä myös yksittäisiäsinä osina. 

Eratostheneen seulaa, sekä Miller-Rabin-algoritmia testataan. Molempia testataan tunnetuilla alkuluvuilla, sekä Miller-Rabinia myös tunnetuista alkuluvuista luoduilla suurilla komposiittiluvuilla. Miller-Rabinin testauksessa käytetään Mersennen alkulukuja kokoluokassa 500-4000 bittiä. Alkuluvut ovat peräisiin kirjallisuudesta, ja ne lasketaan `make_mersenne_primelist.py`-skriptillä.

Koko ohjelmaa päästä-päähän testataan normaalilla tekstisyötteellä, joka enkoodataan kokoaisluvuksi, sekä mahdollisimman suurella kokonaislukusyötteellä. Testit tehdään oletuksena 2048-bitin avaimilla. Testeissä verrataan että purettu (ja dekoodattu) lopputulos vastaa alkuperäistä syötettä. Avaingeneraatiota, salaamista, purkamista, tai tekstienkoodausta ei testata erikseen niiden yksinkertaisuuden vuoksi.

Kattavuustestit voidaan suorittaa paikallisesti ajamalla `tests.sh`-skripti. Skriptin pitäisi toimia yleisimmissä Linux-jakeluissa, joissa asennettuna Bash, Python, sekä Coverage. Yksikkötestit voidaan suorittaa ajamalla `tests.py`-tiedosto, näissä ei Pythonin sisäänrakennettujen kirjastojen ulkopuolisia riippuvuuksia.

Käyttöliittymää (`demo.py`) ei testata.

[Kattavuusraportti](https://github.com/e11-0a/hy-tiralabra-rsa/blob/main/dokumentaatio/coverage.png)
