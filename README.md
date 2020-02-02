# glasovnokontrolisanje-py

#### Jednostavan program za glasovno pokretanje komanda, i diktiranje teksta kodiran u python-u.



### Preduslovi
PIP paketi:
```
pip install SpeechRecognition
```
Kreiranje precice na tastaturi za gasenje/paljenje mikrofona (mute/unmute) kako bi listen.py radio normalno.
```shell
amixer set Capture toggle
```
Ukoliko imate usb mikrofon / webkameru koristite sledecu komandu:
```shell
amixer -c 1 sset Mic toggle
```
Uobicajne komande (pogledajte komande.cfg) 
Za virtualni unos tastature i misa, koristi se
```
xdotool
```
Verovatno ce u sledecim verzijama biti jos vise neophodnih programa.


### Pokretanje
```shell
git clone https://github.com/lizzardguki/glasovnokontrolisanje-py 
cd glasovnokontrolisanje-py/
python main.py
```
Nakon dobijanja poruke '#CEKAM KOMANDU#' 
Izgovorite komandu koja je unapred sacuvana u konfiguracionom fajlu reci.cfg 
I komanda koja je na istom redu u fajlu komande.cfg bice izvrsena.



## Autori

* **Nemanja Vukmirovic** 

## Licence

Ovaj projekat je licenciran pod Apache Licencom 2 - Pogledajte LICENCA.md za detalje.

## Priznanja

Nakon konfiguracije blathera i dosta testiranja sa njim, uopste mi se nije svideo, iz razloga sto sasvim drugacije je osmisljen jos od pocetka kreiranja, primer: Za koriscenje blathera ne treba internet konekcija, dok za koriscenje SpeechRecognition je obavezna.
U blatheru isto nisam uspeo namestiti srpski jezik , dok u ovom projektu zamenite 4 slova i sve uspesno radi.

