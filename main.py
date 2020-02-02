import listen
import os
import mmap
import type
lokacija = (os.path.dirname(os.path.realpath(__file__))) # Dobijamo lokaciju gde se nalazi ovaj fajl.
komande= lokacija + "/" + 'komande.cfg' # Nalazimo tacnu lokaciju fajla komande.cfg.
reci = lokacija + '/' + 'reci.cfg' # Nalazimo tacnu lokaciju fajla reci.cfg.
red = 0 # Variabla koju koristimo za cuvanje broja reda izgovorene reci i nakon toga trazimo u fajlu komande.cfg.

def __main__(t):
        listen.prvopokretanje()
        while t == True: 
            print("Slušam...")                         # Prikazi poruku.
            izgovoreno =  listen.main()                # Pokretanje listen.py.
            if izgovoreno == None:
                print("Nisam uspeo prepoznati.")
            else:
                izgovoreno2 = izgovoreno.replace(" ","_")                # Menjanje razmaka u donju crtu za lakse prepoznavanje slicnih komandi.
                izgovoreno2 = izgovoreno2.lower()                        #Menjanje odgovora u malim slovima (iz razloga sto sve komande pisemo mali slovima).
                print("Proveravam komandu:" + izgovoreno2)               # Prikazi poruku. 
                if izgovoreno2 == "kucaj" or izgovoreno2 =="mod kucanja":# Ako su izgovorene neke od ovih reci pokreni type.py.
                 print ("Ulazim u mod za kucanje.")
                 t = False                                               #/////////////////////////////////////////
                 if type.__main__(True) == False:                        #////////////////////////////////
                        __main__(True)                                   #/////////////////////////////////////////
                try:
                    if nadji_rec(izgovoreno2) == True:                   # Pokretanje funkcije nadji_rec i uporedjivanje rezultata sa Boolom. 
                        try:                                             #
                            red = nadji_red(izgovoreno2)                 # Pokretanje pokusaja trazenja broja reda sa izgovorenom recenicom.
                            try:                                         #
                             red = red -1                             # Mislim da do potrebe ovog reda dolazi zato sto kada citamo linije fajla, sa open , dobijamo niz, a nizovi pocinju od 0, nasuprot brojanjem reda gde nulta linija ne postoji.
                             komanda = nadji_komandu(red)             # Podesavamo string komanda sa rezultatom funkcije nadji_komandu.
                             print ("Komanda pronadjena:" + komanda)  # Prikazi poruku. 
                            except  Exception as e:                      #///////////////
                              print("Greška 3:" + str(e))              # Prikazi gresku. 
                            izvrsi_komandu(komanda)                      # Poziv na funkciju: izvrsi_komandu.
                        except  Exception as e:                          #///////////////
                         print("Greška 2: " + str(e) )                # Prikazi gresku. 
                except  Exception as e:                                  #///////////////
                    print("Greška 1:" + str(e))                          # Prikazi gresku. 

def nadji_rec(rec):                                                # Funkcija za pretragu konfiguracionog fajla reci.cfg.
    bkonvertovano = bytes (rec ,encoding='utf8')                   # Konverotvanje izgovorene reci u binarni kod.
    with open(reci, 'rb', 0) as file, \
        mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s: # reci.cfg se otvara samo za citanje u binarnom formatu, i mapira se u memoriji.
        if s.find(bkonvertovano) != -1:                            # Ako se konvertovana rec nadje u memoriji, nastavi izvrsenje
            with open(reci) as myFile:                             # Ponovno otvaranje konfiguracionog fajla reci.cfg
                for num, line in enumerate(myFile, 1):             # Nabroji sve redove.
                 if rec in line:                                   # Ako je rec u redu .
                    f=open(reci)                                   # Ponovo otvori reci.cfg.
                    linija=f.readlines()                           # Ucitaj sve redove.
                    linija2 = linija[int(num -1)]                  # String linija2 se podesava na broj linije (num -1).
                    linija2 = linija2.strip('\n')                  # Formatiramo tekst da bi izbacili novi red. 
                    linija2 = linija2.strip('\t')                  # //////////////////////////////////////////
                    if rec == linija2:                             # Ako je konacno izgovorena rec jednaka sa ocitanom komandom iz reda (num -1) konfiguracionog fajla reci.cfg .
                        return True                                # Povrati True.
                    else:                                          # U slucaju da nije izvrsi sledece.
                        print("Greška 4 (nepotpuna komanda).")     # Prikazi Gresku.                                
        else:
            print ("Nisam uspeo pronaći komandu.")                 # Prikazi poruku. 

def nadji_red(rec):                            # Trazenje reda u kome se rec nalazi.
    with open(reci) as myFile:                 # Otvori fajl reci.cfg.
        for num, line in enumerate(myFile, 1): # Nabroji sve linije.
            if rec in line:                    # Ako je rec u nekoj liniji.
                return num                     # Povrati broj linije.

def nadji_komandu(red):         # Trazenje komande u fajlu komande.cfg uz pomoc broja reda.
    f=open(komande)             # Otvori fajl komande.cfg.
    linija=f.readlines()        # Procitaj sve linije fajla.
    return (linija[int(red)])   # Povrati komandu sa brojem reda.

def izvrsi_komandu(komanda):   # Funkcija za pokretanje komande.
    os.popen(komanda)          # Pokretanje komande.
    

if __name__ == "__main__":    # Pocetna tacka izvrsenja.
        __main__(True)        # Pokreni funkciju __main__.
