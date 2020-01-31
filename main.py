import listen
import os
import subprocess
import mmap

lokacija = (os.path.dirname(os.path.realpath(__file__)))
komande= lokacija + "/" + 'komande.cfg'
reci = lokacija + '/' + 'reci.cfg'
red = 0
def __main__():
        while True:
            izgovoreno =  listen.main()
            
            try:
                if nadji_rec(izgovoreno) == True:
                    try:
                        red = nadji_red(izgovoreno)
                        try:
                            red = red -1
                            komanda = nadji_komandu(red)
                            print (komanda)
                        except:
                            print("Greska 3")
                        
                        izvrsi_komandu(komanda)
                    except: 
                        print("Greska 2")
            except:
                print("Greska 1")

def nadji_rec(rec):
    bkonvertovano = bytes (rec ,encoding='utf8')
    with open(reci, 'rb', 0) as file, \
        mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
        if s.find(bkonvertovano) != -1:
            with open(reci) as myFile:
                for num, line in enumerate(myFile, 1):
                 if rec in line:
                    f=open(reci)
                    linija=f.readlines()
                    linija2 = linija[int(num -1)]
                    linija2 = linija2.strip('\n')
                    linija2 = linija2.strip('\t')
                    if rec == linija2:
                        return True
                    else:    
                        print("GRESKA(KOD:3)")               
                          
        else:
            print ("NEPOZNATA KOMANDA")

def nadji_red(rec):
    with open(reci) as myFile:
        for num, line in enumerate(myFile, 1):
            if rec in line:

                return num

def nadji_komandu(red):
    f=open(komande)
    linija=f.readlines()
    return (linija[int(red)])

def izvrsi_komandu(komanda):
    os.popen(komanda)
    

if __name__ == "__main__":
        __main__()
