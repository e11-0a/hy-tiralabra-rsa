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

Jos haluaa luoda alkuluvut testiä varten, suorita `make_mersenne_primelist.py` (tunnetut Mersennen alkuluvut väliltä 500-4000 bittiä). (mukana myös skripti `make_probable_primelist.sh`, joka generoi mahdollisia alkulukuja openssl:n avulla, nämä luvut eivät ole vahvistettuja alkulukuja)
