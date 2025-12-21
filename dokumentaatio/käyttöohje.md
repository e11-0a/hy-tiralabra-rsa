# Käyttöohje

Projektin `rsalib.py`-toteutusta voidaan käyttää `demo.py`-skriptillä.

```bash
git clone "https://github.com/e11-0a/hy-tiralabra-rsa"
cd hy-tiralabra-rsa

chmod +x ./demo.py
./demo.py [avaimen pituus bitteinä] [testattava merkkijono]
```

Jos tämä ei toimi voidaan ohjelma myös suorittaa määrittelemällä käytettävä tulkki komennossa:
```
python ./demo.py [avaimen pituus bitteinä] [testattava merkkijono]
```


Ohjelma hyväksyy avaimen pituudeksi kokonaisluvun joka on $\ge 14$. Avaimen maksimikokoa ei rajoiteta, mutta yli 4096-bittisten avaimien luominen on erittäin hidasta. (8192-bittisten alkulukujen luominen vei noin 30 minuuttia modernilla Python 3.14/x86_64/Linux tietokoneella, ja lähemmäs tunnin Python 3.13/ARM64/Linux älypuhelimella).

Salattavan merkkijonon maksimipituutta ei rajoiteta, minimipituus on $\gt 0$. RSA-salaus hajoaa jos salattava data suurempi kuin käytetty modulo. Pituutta ei rajoiteta koska käyttäjä saattaa haluata kokeilla mitä tapahtuu kun yritetään salata liian iso merkkijono.

Ohjelman toiminta vaatii vähintään Pythonin version 3.12 tai uudemman toimiakseen. Tämä rajoitus johtuu pääasiallisesti tästä muutoksesta: https://docs.python.org/3.12/whatsnew/3.12.html#pep-701-syntactic-formalization-of-f-strings. Ohjemaa on kehitetty versioilla 3.13-3.15.

Ohjelmaa on testattu useilla Linux-jakeluilla (Arch, Alpine/postmarketOS ja Cubbli). Ohjelman toimintaa Windows-ympäristössä ei ole testattu.

Esimerkki ohjelman suorituksesta:

```
$ ./demo.py 512 "Hello World!"

Generating two 512-bit primes:

Prime 1          (p): 12478648928495117903185386475618900116273852236363197463117045161925741137301204860810943048015244636867384517789524104744938011965058644360111843202330247
Prime 2          (q): 11910296747156415572933508053654901068754289672428023972078295008597987834817525786167699788489538900086227604282785414440998327321281396186161061796546741

Generating keypair:
Modulo           (N): 148624411741962293389277039718018057967888435354721563401435748458954152395576572050377152243330907548508033688120027212718908864818040670617922667419253831388357550476842120529321791032903010019750583317676588535357922934033228797211940736502697728637438982603029791784500967761097057321367552231228853575027
Public  exponent (e): 65537
Private exponent (d): 119916408198292295189559963169039761802127114220775544036820719700513872627268534978406748192972698313166727274065196743124501624332031594075629259926382086554387614889492508035683243775238205928044974466482988209918957412638181250968671915530368216350254535437710276491113213289127384743741846911885633897233

Encoding message to an integer:
Original message    : Hello World!
Encoded message     : 1406976767900557982766801

Encrypting the message:
Encrypted message   : 27296652461032558398807730548014715027364475487887547927377743879149668107905785639647983587769394515146260740587441368350909298586596372571616935155875071958204775397041566707054788569411582480598594624726586897838619542653585716042937956582396196660098255287484750483485528390260482553201315702402480527561

Decrypting the message:
Decrypted message   : 1406976767900557982766801

Decoding the message:
Decoded message     : Hello World!

The input string is smaller than the modulo: Yes
The decrypted message matches the original : Yes
The decoded message matches the original   : Yes
```



## Testien ajaminen

*Riippuvuutena coverage, asenna jakelusi pakettienhallinnalla (esim `python-coverage` archilla) tai luo python virtuaaliympäristö ja asenna pip:llä (`pip install coverage`).*

```bash
chmod +x ./tests.sh
./tests.sh
```
Jos ei avaudu automaattisesti voi raportin myös avata käsin polusta `htmlcov/index.html`.

Jos haluaa luoda alkuluvut testiä varten, suorita `make_mersenne_primelist.py` (tunnetut Mersennen alkuluvut väliltä 500-4000 bittiä). (mukana myös skripti `make_probable_primelist.sh`, joka generoi mahdollisia alkulukuja openssl:n avulla, nämä luvut eivät ole vahvistettuja alkulukuja)
