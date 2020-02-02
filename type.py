import listen
import os
def __main__(t):
     while t == True:       
            izgovoreno =  listen.main()                     # Pokreni listen.
            print (izgovoreno)                              # Prikazi izgovoreno.
            if izgovoreno == "" or izgovoreno == None:                                  # Ako nista nije izgovoreno: 
                print("Nisam prepoznato")                                               # Istampaj poruku.
            elif izgovoreno == "prekini kucanje" or izgovoreno == "stop" or izgovoreno == "prekid" or izgovoreno == "prekini"  or izgovoreno == "prekid" :  # Uporedi izgovoreno za datim komandama. 
                return False
            elif izgovoreno == "znak zarez" or izgovoreno == "znak zapeta":             # Uporedi izgovoreno za datim komandama.
                try:
                    os.popen('xdotool type ", " ')                                      # Izvrsi komandu.
                except Exception as e:                                                  # Ako dodje do greske nastavi odavde.
                    print("Greška prilikom pokušaja kucanja zareza(zapete): " + str(e)) # Istampaj poruku.
            elif izgovoreno == "znak tačka":                                            # Uporedi izgovoreno za datim komandama.
                try:
                    os.popen('xdotool type ". " ')                                         # Izvrsi komandu.
                except Exception as e:                                                     # Ako dodje do greske nastavi odavde.
                    print("Greška prilikom pokušaja kucanja tačke: " + str(e))             # Istampaj poruku.
            elif izgovoreno == "znak dve tačke":                                           # Uporedi izgovoreno za datim komandama.
                try:
                    os.popen('xdotool type ": " ')                                         # Izvrsi komandu.
                except Exception as e:                                                     # Ako dodje do greske nastavi odavde.
                    print("Greška prilikom pokušaja kucanja dve tačke: " + str(e))         # Istampaj poruku.
            elif izgovoreno == "znak tačka zarez":                                         # Uporedi izgovoreno za datim komandama.
                try:
                    os.popen('xdotool type "; " ')                                         # Izvrsi komandu.
                except Exception as e:                                                     # Ako dodje do greske nastavi odavde.
                    print("Greška prilikom pokušaja kucanja tačke zareza: " + str(e))      # Istampaj poruku.    
            elif izgovoreno == "znak razmak":                                              # Uporedi izgovoreno za datim komandama.
                try:
                    os.popen('xdotool type " " ')                                          # Izvrsi komandu.
                except Exception as e:                                                     # Ako dodje do greske nastavi odavde.
                    print("Greška prilikom pokušaja kucanja razmaka: " + str(e))           # Istampaj poruku.
            elif izgovoreno == "znak uzvičnik":                                            # Uporedi izgovoreno za datim komandama.  
                try:
                    os.popen('xdotool type "! " ')                                         # Izvrsi komandu.
                except Exception as e:                                                     # Ako dodje do greske nastavi odavde.
                    print("Greška prilikom pokušaja kucanja uzvičnika : " + str(e))        # Istampaj poruku.
            elif izgovoreno == "znak upitnik":                                             # Uporedi izgovoreno za datim komandama.
                try:
                    os.popen('xdotool type "? " ')                                         # Izvrsi komandu.
                except Exception as e:                                                     # Ako dodje do greske nastavi odavde.
                    print("Greška prilikom pokušaja kucanja upitnika : " + str(e))         # Istampaj poruku.
            elif izgovoreno == "otvori zagradu":                                           # Uporedi izgovoreno za datim komandama.
                try:
                    os.popen('xdotool type "(" ')                                          # Izvrsi komandu.
                except Exception as e:                                                     # Ako dodje do greske nastavi odavde.
                    print("Greška prilikom pokušaja kucanja otvorene zagrade : " + str(e)) # Istampaj poruku.
            elif izgovoreno == "zatvori zagradu":                                          # Uporedi izgovoreno za datim komandama.
                try:
                    os.popen('xdotool type ")" ')                                          # Izvrsi komandu.
                except Exception as e:                                                     # Ako dodje do greske nastavi odavde.
                    print("Greška prilikom pokušaja kucanja zatvorene zagrade : " + str(e))# Istampaj poruku.
            elif izgovoreno == "znak jednako":                                             # Uporedi izgovoreno za datim komandama.
                
                try:
                    os.popen('xdotool type "=" ')                                          # Izvrsi komandu.
                except Exception as e:                                                     # Ako dodje do greske nastavi odavde.
                    print("Greška prilikom pokušaja kucanja znaka jednako : " + str(e))    # Istampaj poruku.
            elif izgovoreno == "znak plus":                                                # Uporedi izgovoreno za datim komandama.
                try:
                    os.popen('xdotool type "+" ')                                          # Izvrsi komandu.
                except Exception as e:                                                     # Ako dodje do greske nastavi odavde.
                    print("Greška prilikom pokušaja kucanja znaka plus : " + str(e))       # Istampaj poruku.
            elif izgovoreno == "briši" or izgovoreno == "obriši":                          # Uporedi izgovoreno za datim komandama.
                try:
                    os.popen('xdotool key BackSpace ')                                     # Izvrsi komandu.
                except Exception as e:                                                     # Ako dodje do greske nastavi odavde.
                    print("Greška prilikom pokušaja brisanja: " + str(e))                  # Istampaj poruku.
            elif izgovoreno == "novi red" :                                                # Uporedi izgovoreno za datim komandama.
                try:
                    os.popen('xdotool key Return ')                                        # Izvrsi komandu.
                except Exception as e:                                                     # Ako dodje do greske nastavi odavde.
                    print("Greška prilikom pokušaja brisanja: " + str(e))                  # Istampaj poruku.                                  
            else:                                                                          # Ako se izgovoreno ne podudara ni sa jednom komandom, nastavi odavde.
                print(izgovoreno)                                                          # Istampaj izgovoreno.
                try:
                    os.popen('xdotool type "' + izgovoreno + ' " ')                        # Pokusaj ukucati zgovoreno uz pomoc xdotool-a.
                except Exception as e:                                                     # Ako dodje do greske nastavi odavde.
                    print("Greška prilikom pokušaja kucanja: " + str(e))                   # Istampaj poruku..

if __name__ == "__main__":
        __main__(True)
