# hy-tiralabra-rsa

Demon testaaminen:
```bash
chmod +x ./demo.py
./demo.py [avaimen pituus bitteinä] [testattava merkkijono]
```

Testien ajaminen:
<br>
*Riippuvuutena coverage, asenna jakelusi pakettienhallinnalla (esim `python-coverage` archilla) tai luo python virtuaaliympäristö ja asenna pip:llä (`pip install coverage`).*

```bash
chmod +x ./tests.sh
./tests.sh
```
Jos ei avaudu automaattisesti voi raportin myös avata käsin polusta `htmlcov/index.html`.

Jos haluaa luoda uudet alkuluvut testiä varten, suorita `make_primelist.sh`. (tässä riippuvuutena openssl)

```bash
chmod +x ./make_primelist.sh
./make_primelist.sh
```